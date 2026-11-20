#!/usr/bin/env python3
"""Prüft eine Netzwerkkonfiguration im Format von /etc/network/interfaces (Beispiel angelehnt an die Proxmox-Dokumentation, aber erfunden) auf einfache Fehler:
Bridge ohne bridge-ports, fehlendes bridge-stp/bridge-fd, mehrere Gateways, eine Schnittstelle in zwei Bridges, NAT ohne Weiterleitung."""
import re, sys
def lies(pfad):
    blocks, cur = {}, None
    for z in open(pfad, encoding='utf-8'):
        z = z.rstrip()
        m = re.match(r'iface (\S+) inet (\S+)', z)
        if m: cur = blocks.setdefault(m.group(1), {'inet': m.group(2), 'opt': {}, 'zeilen': []}); continue
        if cur is not None and z.startswith((' ', '\t')) and z.strip():
            k, _, v = z.strip().partition(' '); cur['opt'][k] = v.strip(); cur['zeilen'].append(z.strip())
    return blocks
if __name__ == '__main__':
    b = lies(sys.argv[1] if len(sys.argv) > 1 else 'interfaces'); m = []; ports = {}
    for n, i in b.items():
        if not n.startswith('vmbr'): continue
        o = i['opt']
        if 'bridge-ports' not in o: m.append('%s: bridge-ports fehlt' % n)
        for p in o.get('bridge-ports', 'none').split():
            if p != 'none': ports.setdefault(p, []).append(n)
        if 'bridge-stp' not in o or 'bridge-fd' not in o: m.append('%s: bridge-stp oder bridge-fd fehlt (laut Dokumentation üblich: stp off, fd 0)' % n)
        if any('MASQUERADE' in z for z in i['zeilen']) and not any('ip_forward' in z for z in i['zeilen']): m.append('%s: NAT ohne ip_forward' % n)
    for p, bs in ports.items():
        if len(bs) > 1: m.append('Schnittstelle %s in mehreren Bridges: %s' % (p, ', '.join(bs)))
    gw = [n for n, i in b.items() if 'gateway' in i['opt']]
    if len(gw) > 1: m.append('mehrere Gateways: ' + ', '.join(gw))
    print('Gefundene Schnittstellenblöcke: %s' % ', '.join(b))
    print('\n'.join('  Hinweis: ' + x for x in m) or '  keine Auffälligkeiten')

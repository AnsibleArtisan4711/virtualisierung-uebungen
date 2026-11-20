#!/usr/bin/env python3
"""Liest eine VM-Konfiguration (Zeilen „schlüssel: wert“, erfundenes Beispiel; Aufbau aus Fachwissen, nicht gegen die Dokumentation geprüft) und prüft einfache Regeln:
Pflichtfelder, Speicher größer als 512 MB, virtio für Netzwerk und Platte, Gast-Agent aktiv, Netzwerkkarte mit Bridge, keine zwei Platten auf dem gleichen Volume."""
import sys
def lies(pfad):
    d = {}
    for z in open(pfad, encoding='utf-8'):
        z = z.rstrip('\n')
        if not z or z.startswith('#') or z.startswith('['): continue
        k, _, v = z.partition(':'); d[k.strip()] = v.strip()
    return d
if __name__ == '__main__':
    c = lies(sys.argv[1] if len(sys.argv) > 1 else '100.conf'); m = []
    for k in ('name', 'memory', 'cores', 'scsi0', 'net0'):
        if k not in c: m.append('Pflichtfeld fehlt: ' + k)
    if int(c.get('memory', 0)) < 512: m.append('Speicher unter 512 MB')
    if not c.get('net0', '').startswith('virtio'): m.append('Netzwerkkarte ist nicht virtio (langsamer)')
    if 'bridge=' not in c.get('net0', ''): m.append('net0 ohne Bridge')
    if c.get('agent', '0') != '1': m.append('Gast-Agent nicht aktiviert')
    if 'virtio-scsi' not in c.get('scsihw', ''): m.append('SCSI-Controller nicht virtio-scsi')
    vols = [v.split(',')[0] for k, v in c.items() if k.startswith(('scsi', 'sata', 'virtio', 'ide')) and 'media=cdrom' not in v]
    if len(vols) != len(set(vols)): m.append('Volume doppelt eingebunden')
    print('VM %s: %d MB, %s Kerne' % (c.get('name', '?'), int(c.get('memory', 0)), c.get('cores', '?')))
    print('\n'.join('  Hinweis: ' + x for x in m) or '  alle Regeln erfüllt')

#!/usr/bin/env python3
"""Liest eine Speicherkonfiguration im Format von /etc/pve/storage.cfg (erfundenes Beispiel) und prüft, ob die eingetragenen Inhaltstypen zum Speichertyp passen.
Die Tabelle erlaubter Inhaltstypen stammt aus der Proxmox-VE-Dokumentation (Kapitel Storage, gelesen über einen Auszug am 20.11.2026); Einträge außerhalb der Tabelle (z. B. btrfs) werden nicht geprüft."""
import sys
ERLAUBT = {'dir': {'images', 'rootdir', 'vztmpl', 'iso', 'backup', 'snippets'}, 'nfs': {'images', 'rootdir', 'vztmpl', 'iso', 'backup', 'snippets'},
           'cifs': {'images', 'rootdir', 'vztmpl', 'iso', 'backup', 'snippets'}, 'lvm': {'images', 'rootdir'}, 'lvmthin': {'images', 'rootdir'},
           'zfspool': {'images', 'rootdir'}, 'pbs': {'backup'}, 'cephfs': {'vztmpl', 'iso', 'backup', 'snippets'}, 'rbd': {'images', 'rootdir'}}
def lies(pfad):
    s, aktuell = [], None
    for z in open(pfad, encoding='utf-8'):
        if not z.strip(): continue
        if not z[0].isspace():
            typ, name = z.strip().rstrip(':').split(':'); aktuell = {'typ': typ.strip(), 'name': name.strip()}; s.append(aktuell)
        else:
            k, _, v = z.strip().partition(' '); aktuell[k] = v.strip()
    return s
if __name__ == '__main__':
    n = 0
    for e in lies(sys.argv[1] if len(sys.argv) > 1 else 'storage.cfg'):
        inh = set(e.get('content', '').split(',')) - {''}; erl = ERLAUBT.get(e['typ'])
        if erl is None: print('%-10s %-9s Typ nicht in der Tabelle: nicht geprüft' % (e['name'], e['typ'])); continue
        zuviel = inh - erl
        if zuviel: n += 1; print('%-10s %-9s FALSCH: %s nicht möglich für Typ %s' % (e['name'], e['typ'], ', '.join(sorted(zuviel)), e['typ']))
        else: print('%-10s %-9s ok: %s' % (e['name'], e['typ'], ','.join(sorted(inh))))
    print('\nEinträge mit Fehlern: %d' % n)

#!/usr/bin/env python3
"""Modell eines Standard-vSwitch mit Portgruppen und VLAN-Nummern (erfundene Konfiguration; Begriffe aus Fachwissen, nicht gegen Herstellerdokumentation geprüft).
Prüft: VM-Adapter verweist auf vorhandene Portgruppe; VLAN-ID 0..4095 zulässig; Portgruppen-Namen eindeutig; vSwitch mit Uplink."""
VSWITCH = {'vSwitch0': {'uplinks': ['vmnic0'], 'portgruppen': {'Management': 0, 'VM Network': 0, 'DMZ': 20, 'Test': 30}},
           'vSwitch1': {'uplinks': [], 'portgruppen': {'Intern': 40, 'Kaputt': 5000}}}
VMS = {'web01': 'DMZ', 'db01': 'Intern', 'test01': 'Test2', 'dc01': 'VM Network'}
def pruefe():
    m = []; alle = {}
    for s, c in VSWITCH.items():
        if not c['uplinks']: m.append('%s: kein Uplink – nur interner Verkehr, keine Verbindung nach außen' % s)
        for pg, v in c['portgruppen'].items():
            if pg in alle: m.append('Portgruppe %s doppelt (%s, %s)' % (pg, alle[pg], s))
            alle[pg] = s
            if not 0 <= v <= 4095: m.append('%s/%s: VLAN-ID %d unzulässig' % (s, pg, v))
    for vm, pg in VMS.items():
        if pg not in alle: m.append('VM %s: Portgruppe "%s" existiert nicht' % (vm, pg))
    return m
if __name__ == '__main__':
    for s, c in VSWITCH.items(): print('%s  Uplinks: %s  Portgruppen: %s' % (s, ', '.join(c['uplinks']) or '-', ', '.join('%s(VLAN %d)' % x for x in c['portgruppen'].items())))
    print(); print('\n'.join('Hinweis: ' + x for x in pruefe()) or 'alle Regeln erfüllt')

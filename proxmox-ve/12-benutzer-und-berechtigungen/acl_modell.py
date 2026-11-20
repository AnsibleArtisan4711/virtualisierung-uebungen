#!/usr/bin/env python3
"""Einfaches Modell der Rechteprüfung mit Rollen und Pfaden (erfundene Daten; Aufbau ANGELEHNT an das Prinzip „Benutzer + Rolle + Pfad“ bei Proxmox VE).
NICHT gelesen/nicht bestätigt: genaue Rollennamen, Rechte-Liste und Vererbungsregeln der echten Software – hier nur ein Übungsmodell. Rechte gelten am Pfad und werden an Unterpfade vererbt."""
ROLLEN = {'Betrachter': {'Ansicht'}, 'Operator': {'Ansicht', 'Energie'}, 'Verwalter': {'Ansicht', 'Energie', 'Konfig', 'Anlegen'}}
# (Benutzer, Pfad, Rolle)
ZUWEISUNG = [('anna', '/vm', 'Betrachter'), ('anna', '/vm/100', 'Operator'), ('ben', '/vm', 'Verwalter'), ('cem', '/speicher', 'Betrachter')]
def darf(benutzer, pfad, recht):
    teile = pfad.strip('/').split('/'); kandidaten = ['/' + '/'.join(teile[:i]) for i in range(len(teile), 0, -1)]
    for k in kandidaten:                       # tiefster passender Pfad zuerst
        r = {z[2] for z in ZUWEISUNG if z[0] == benutzer and z[1] == k}
        if r: return recht in set().union(*[ROLLEN[x] for x in r]), k
    return False, None
if __name__ == '__main__':
    print('%-6s %-10s %-8s %-8s %s' % ('Nutzer', 'Pfad', 'Recht', 'Ergebnis', 'Grund'))
    for b, p, r in [('anna', '/vm/100', 'Energie'), ('anna', '/vm/101', 'Energie'), ('anna', '/vm/101', 'Ansicht'), ('ben', '/vm/100', 'Konfig'), ('cem', '/vm/100', 'Ansicht'), ('cem', '/speicher/lokal', 'Ansicht')]:
        ok, k = darf(b, p, r); print('%-6s %-10s %-8s %-8s %s' % (b, p, r, 'ERLAUBT' if ok else 'NEIN', ('über ' + k) if k else 'keine Zuweisung'))

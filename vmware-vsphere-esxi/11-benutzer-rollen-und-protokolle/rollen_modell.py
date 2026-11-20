#!/usr/bin/env python3
"""Einfaches Modell: Benutzer, Rollen und Objekte (Host, Datastore, VM-Ordner) mit Vererbung (erfundene Daten; Aufbau aus Fachwissen, NICHT gegen Herstellerdokumentation geprüft).
Prüft zusätzlich eine Liste von Protokollzeilen auf Anmeldefehlschläge je Benutzer (Hinweis auf Angriff oder falsches Kennwort)."""
ROLLEN = {'Nur-Lesen': {'ansehen'}, 'Operator': {'ansehen', 'ein/aus'}, 'Admin': {'ansehen', 'ein/aus', 'ändern'}}
ZUW = [('anna', 'ordner/produktion', 'Operator'), ('ben', '', 'Admin'), ('cem', 'ordner/test', 'Admin')]
def darf(nutzer, objekt, recht):
    teile = objekt.split('/') if objekt else []
    for i in range(len(teile), -1, -1):
        pfad = '/'.join(teile[:i]); r = [z[2] for z in ZUW if z[0] == nutzer and z[1] == pfad]
        if r: return recht in ROLLEN[r[0]], pfad or 'Wurzel'
    return False, None
LOG = ['Anmeldung fehlgeschlagen: root von 10.7.0.99', 'Anmeldung fehlgeschlagen: root von 10.7.0.99', 'Anmeldung ok: anna', 'Anmeldung fehlgeschlagen: root von 10.7.0.99', 'Anmeldung fehlgeschlagen: anna von 10.7.0.5']
if __name__ == '__main__':
    print('%-5s %-22s %-8s %s' % ('Nutzer', 'Objekt', 'Recht', 'Ergebnis')); 
    for n, o, r in [('anna', 'ordner/produktion/web01', 'ein/aus'), ('anna', 'ordner/produktion/web01', 'ändern'), ('anna', 'ordner/test/x', 'ansehen'), ('ben', 'ordner/test/x', 'ändern'), ('cem', 'ordner/produktion/db01', 'ansehen')]:
        ok, p = darf(n, o, r); print('%-5s %-22s %-8s %s' % (n, o, r, ('ERLAUBT über ' + p) if ok else 'NEIN'))
    z = {}
    for l in LOG:
        if l.startswith('Anmeldung fehlgeschlagen'): k = l.split(': ')[1]; z[k] = z.get(k, 0) + 1
    print('\nFehlschläge:', ', '.join('%s x%d' % x for x in z.items())); [print('Warnung: %s (mindestens 3 Fehlschläge)' % k) for k, v in z.items() if v >= 3]

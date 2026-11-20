#!/usr/bin/env python3
"""Verteilt CPU-Zeit nach „Shares“, wenn ein Host überlastet ist, und prüft Reservierungen (erfundene Werte; Verfahren vereinfacht, aus Fachwissen, NICHT gegen Herstellerdokumentation geprüft).
Modell: Jede VM bekommt zuerst ihre Reservierung; der Rest wird nach Shares verteilt, begrenzt durch ein Limit; Reservierungen dürfen die Gesamtkapazität nicht übersteigen."""
HOST_MHZ = 8000
VMS = {'db01': dict(shares=2000, res=2000, limit=None, bedarf=6000), 'web01': dict(shares=1000, res=500, limit=3000, bedarf=4000), 'test01': dict(shares=500, res=0, limit=1000, bedarf=3000)}
def verteile():
    if sum(v['res'] for v in VMS.values()) > HOST_MHZ: raise SystemExit('Reservierungen übersteigen die Kapazität')
    erg = {n: min(v['res'], v['bedarf']) for n, v in VMS.items()}; rest = HOST_MHZ - sum(erg.values())
    aktiv = {n for n, v in VMS.items() if erg[n] < min(v['bedarf'], v['limit'] or 10**9)}
    while rest > 1e-9 and aktiv:
        sh = sum(VMS[n]['shares'] for n in aktiv); neu = set(); gab = 0
        for n in sorted(aktiv):
            v = VMS[n]; ziel = min(v['bedarf'], v['limit'] or 10**9); gib = min(rest * v['shares'] / sh, ziel - erg[n]); erg[n] += gib; gab += gib
            if erg[n] < ziel - 1e-9: neu.add(n)
        rest -= gab; aktiv = neu
        if gab < 1e-9: break
    return erg
if __name__ == '__main__':
    e = verteile(); print('%-7s %7s %6s %7s %7s %8s' % ('VM', 'Shares', 'Res.', 'Limit', 'Bedarf', 'Zuteilung'))
    for n, v in VMS.items(): print('%-7s %7d %6d %7s %7d %8.0f MHz' % (n, v['shares'], v['res'], v['limit'] or '-', v['bedarf'], e[n]))
    print('Summe: %.0f von %d MHz' % (sum(e.values()), HOST_MHZ))

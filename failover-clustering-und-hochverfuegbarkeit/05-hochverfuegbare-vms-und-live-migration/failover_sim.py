#!/usr/bin/env python3
"""Modell: Knotenausfall. VMs werden nach Priorität auf Knoten mit genug freiem RAM neu gestartet (First-Fit). Vereinfacht: nur RAM, erfundene Werte."""
knoten = {"hv01": 64, "hv02": 64, "hv03": 64}
vms = [("dc-test", 8, "hoch", "hv01"), ("db1", 32, "hoch", "hv01"), ("web1", 16, "mittel", "hv01"),
       ("app1", 24, "mittel", "hv02"), ("web2", 16, "mittel", "hv02"), ("file1", 16, "niedrig", "hv03"), ("test1", 24, "niedrig", "hv03")]
def lauf(ausfall):
    frei = {k: r for k, r in knoten.items() if k != ausfall}
    for n, r, p, h in vms:
        if h in frei: frei[h] -= r
    print(f"\nAusfall von {ausfall}: freier RAM auf den übrigen Knoten {frei}")
    prio = {"hoch": 0, "mittel": 1, "niedrig": 2}
    for n, r, p, h in sorted((v for v in vms if v[3] == ausfall), key=lambda v: prio[v[2]]):
        ziel = next((k for k in sorted(frei) if frei[k] >= r), None)
        if ziel: frei[ziel] -= r; print(f"  {n:<8} ({p}, {r} GB) -> {ziel}")
        else: print(f"  {n:<8} ({p}, {r} GB) -> KEIN Platz, bleibt aus")
for k in ("hv01", "hv02"): lauf(k)

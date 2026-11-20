#!/usr/bin/env python3
"""Modell: rollierende Aktualisierung (Cluster-aware Updating). Je Knoten: leeren, patchen, zurück; prüft, ob die VMs auf den übrigen Knoten Platz haben. Erfundene Werte."""
knoten = {"hv01": 64, "hv02": 64, "hv03": 64}
belegt = {"hv01": 40, "hv02": 36, "hv03": 30}
for k in knoten:
    uebrig = sum(knoten[x] - belegt[x] for x in knoten if x != k)
    ok = uebrig >= belegt[k]
    print(f"{k}: leeren ({belegt[k]} GB RAM verschieben) -> freier Platz übrig {uebrig} GB -> {'patchen, dann zurück' if ok else 'ABBRUCH: nicht genug Platz'}")
print("\nGesamtbelegung:", sum(belegt.values()), "GB von", sum(knoten.values()), "GB; für N+1 muss sie unter", sum(knoten.values()) - max(knoten.values()), "GB liegen.")

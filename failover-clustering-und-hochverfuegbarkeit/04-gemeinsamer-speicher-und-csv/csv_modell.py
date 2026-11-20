#!/usr/bin/env python3
"""Modell: Cluster Shared Volume (CSV). Alle Knoten greifen auf dasselbe Volume zu; ein Knoten ist Koordinator. Platzplanung mit Reserve. Erfundene Werte."""
volume_gb = 2000; reserve = 0.20
vms = {"web1": 120, "web2": 120, "db1": 600, "app1": 250, "file1": 500}
summe = sum(vms.values()); frei = volume_gb * (1 - reserve) - summe
print(f"Volume {volume_gb} GB, Reserve {int(reserve*100)} %, nutzbar {volume_gb*(1-reserve):.0f} GB")
for n, g in vms.items(): print(f"  {n:<6} {g:>5} GB")
print(f"Summe der virtuellen Festplatten: {summe} GB -> {'Platz reicht' if frei >= 0 else 'zu wenig Platz'}, frei {frei:.0f} GB")
knoten = ["hv01", "hv02", "hv03"]; koord = "hv01"
print("\nKoordinator vor dem Ausfall:", koord)
knoten.remove("hv01"); koord = knoten[0]
print("hv01 fällt aus -> neuer Koordinator (einfaches Modell: erster verbleibender Knoten):", koord)
print("Zugriff der übrigen Knoten bleibt direkt; nur die Verwaltung der Metadaten wandert.")

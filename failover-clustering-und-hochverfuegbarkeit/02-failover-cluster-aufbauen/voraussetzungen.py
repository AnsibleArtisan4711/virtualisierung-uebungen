#!/usr/bin/env python3
"""Modell: prüft eine erfundene Bestandsliste gegen Voraussetzungen für einen Failovercluster (eigene Beispielregeln, keine amtliche Prüfliste)."""
knoten = [
  {"name": "hv01", "os": "Windows Server 2022", "domaene": "lab.example", "nics": 3, "speicher": True,  "ram_gb": 32},
  {"name": "hv02", "os": "Windows Server 2022", "domaene": "lab.example", "nics": 3, "speicher": True,  "ram_gb": 32},
  {"name": "hv03", "os": "Windows Server 2019", "domaene": "lab.example", "nics": 1, "speicher": False, "ram_gb": 16},
]
def pruefe(k, ref):
    f = []
    if k["os"] != ref["os"]: f.append(f"Betriebssystem {k['os']} weicht von {ref['os']} ab")
    if k["domaene"] != ref["domaene"]: f.append("nicht in derselben Domäne")
    if k["nics"] < 2: f.append("weniger als 2 Netzwerkkarten (Verwaltung/Cluster getrennt empfohlen)")
    if not k["speicher"]: f.append("gemeinsamer Speicher nicht sichtbar")
    if k["ram_gb"] != ref["ram_gb"]: f.append(f"RAM {k['ram_gb']} GB statt {ref['ram_gb']} GB (ungleich)")
    return f
ref = knoten[0]
for k in knoten:
    f = pruefe(k, ref)
    print(f"{k['name']}: " + ("ok" if not f else "; ".join(f)))
print("\nCluster möglich:", "ja" if all(not pruefe(k, ref) for k in knoten) else "nein - Punkte oben beheben")

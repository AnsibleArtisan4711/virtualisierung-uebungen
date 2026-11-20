#!/usr/bin/env python3
"""Modell: Verfügbarkeit in Prozent -> Ausfallzeit pro Jahr; Reihen- und Parallelschaltung. Erfundene Werte, reine Rechnung."""
MIN_JAHR = 365 * 24 * 60
print("Verfügbarkeit  erlaubte Ausfallzeit pro Jahr")
for p in (99.0, 99.9, 99.99, 99.999):
    m = MIN_JAHR * (1 - p / 100)
    print(f"{p:>9}%     {m:9.1f} Minuten" + (f" (= {m/60:.1f} Stunden)" if m >= 60 else ""))
a, b = 0.999, 0.999
print("\nReihenschaltung (beide Teile müssen laufen): 0.999 * 0.999 =", f"{a*b:.6f}")
print("Parallelschaltung (eines genügt):            1-(1-0.999)^2 =", f"{1-(1-a)*(1-b):.6f}")
print("\nKette: Cluster-Knoten 2x 99,9 % parallel, davor ein einzelner Switch mit 99,9 %:")
k = (1 - (1 - a) * (1 - b)) * 0.999
print(f"  Gesamt {k*100:.4f} %  -> der einzelne Switch begrenzt die Gesamtverfügbarkeit")

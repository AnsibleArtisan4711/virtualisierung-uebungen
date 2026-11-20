#!/usr/bin/env python3
"""Modell: Quorum nach einfacher Mehrheit der Stimmen. Dynamisches Quorum und Zeugen-Besonderheiten werden NICHT nachgebildet (Fachwissen prüfen)."""
from itertools import combinations
def pruefe(knoten, zeuge):
    stimmen = knoten + (1 if zeuge else 0)
    mehrheit = stimmen // 2 + 1
    ueberlebt = {}
    elemente = [f"K{i+1}" for i in range(knoten)] + (["Z"] if zeuge else [])
    for ausfall in range(0, len(elemente)):
        ok = 0; n = 0
        for ausgefallen in combinations(elemente, ausfall):
            n += 1
            if stimmen - len(ausgefallen) >= mehrheit: ok += 1
        ueberlebt[ausfall] = (ok, n)
    return stimmen, mehrheit, ueberlebt
print("Knoten Zeuge Stimmen Mehrheit  Ausfälle -> Fälle mit Quorum / alle Fälle")
for kn, z in ((2, False), (2, True), (3, False), (4, False), (4, True), (5, False)):
    s, m, u = pruefe(kn, z)
    teile = " ".join(f"{a}:{ok}/{n}" for a, (ok, n) in u.items() if a > 0)
    print(f"{kn:>6} {'ja' if z else 'nein':>6} {s:>7} {m:>8}   {teile}")

#!/usr/bin/env python3
"""Modell: Replikation mit festem Intervall. Schlimmster Datenverlust (RPO) ~ Intervall + Dauer der Übertragung; Datenmenge je Zyklus aus Änderungsrate. Erfundene Werte."""
aenderung_mb_min = 40; leitung_mb_s = 5
print("Intervall   Daten je Zyklus   Übertragung   schlimmster Verlust (ca.)")
for intervall_min in (0.5, 5, 15):
    mb = aenderung_mb_min * intervall_min
    sek = mb / leitung_mb_s
    print(f"{intervall_min:>6} min   {mb:>9.0f} MB   {sek:>8.0f} s   {intervall_min*60 + sek:>8.0f} s")
print("\nÜbertragung länger als das Intervall? ->", "ja, die Replikation gerät in Rückstand" if aenderung_mb_min / 60 > leitung_mb_s else "nein")

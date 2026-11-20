#!/usr/bin/env python3
"""Modell: Testplan für Ausfalltests. Prüft, ob jede Ausfallart (hier eine erfundene Liste) durch mindestens einen Test abgedeckt ist."""
ausfallarten = ["Knoten", "Netzwerk Cluster", "Netzwerk Verwaltung", "Speicherpfad", "Zeuge", "Dienst auf VM"]
tests = [("T1 Knoten hart ausschalten", "Knoten"), ("T2 Cluster-Netzwerkkabel ziehen", "Netzwerk Cluster"),
         ("T3 Zeugen abschalten", "Zeuge"), ("T4 Speicherpfad trennen", "Speicherpfad"), ("T5 Live-Migration anstoßen", None)]
abgedeckt = {a: [t for t, x in tests if x == a] for a in ausfallarten}
for a, t in abgedeckt.items(): print(f"{a:<22} {'; '.join(t) if t else 'KEIN TEST'}")
print("\nLücken:", ", ".join(a for a, t in abgedeckt.items() if not t))

#!/usr/bin/env python3
"""Ordnet Meldungen einer wahrscheinlichen Ursache und ersten Prüfung zu. Regeln sind Erfahrungswerte aus Fachwissen, NICHT gegen Herstellerdokumentation geprüft; Beispielzeilen sind erfunden.
Aufruf: fehler_zuordnen.py [protokoll.txt]"""
import re, sys
REGELN = [
 (r'no space left|datastore .* full|insufficient disk space', 'Datastore voll', 'Belegung je Datastore, Snapshots und dünne Platten prüfen (datastore_rechner.py)'),
 (r'network .* not found|portgroup .* not found', 'Portgruppe fehlt', 'Portgruppen und VM-Adapter vergleichen (portgruppen_pruefen.py)'),
 (r'failed to power on|insufficient (memory|cpu) resources', 'zu wenig Ressourcen oder Reservierung', 'Reservierungen und freie Kapazität prüfen (ressourcen_rechner.py)'),
 (r'license|lizenz', 'Lizenz/Funktion nicht verfügbar', 'Lizenzstand prüfen (gratis_grenzen_pruefen.py)'),
 (r'authentication failure|login failed|anmeldung fehlgeschlagen', 'Anmeldung fehlgeschlagen', 'Benutzer, Rolle, Sperren prüfen (rollen_modell.py)'),
 (r'vmdk .* (corrupt|not found|locked)|could not open/create change tracking file', 'Platte/Sperre/Snapshot-Kette', 'Dateien im Datastore und Kette prüfen (snapshot_kette.sh)'),
]
BEISPIEL = """2026-11-20T10:01:11Z vmx: Failed to power on VM web01: insufficient memory resources
2026-11-20T10:02:03Z hostd: Task failed: Network "Test2" not found
2026-11-20T10:03:44Z vpxa: Datastore datastore1 full - no space left on device
2026-11-20T10:04:10Z hostd: Anmeldung fehlgeschlagen: root von 10.7.0.99
2026-11-20T10:05:00Z hostd: Operation requires license: vMotion
2026-11-20T10:06:30Z vmkernel: cpu3:12345)Heartbeat: ok
"""
text = open(sys.argv[1]).read() if len(sys.argv) > 1 else BEISPIEL
for z in text.splitlines():
    print('ZEILE  :', z[:100])
    for mu, u, p in REGELN:
        if re.search(mu, z, re.I): print('URSACHE:', u); print('PRÜFEN :', p); break
    else: print('URSACHE: unbekannt (keine Regel)')
    print()

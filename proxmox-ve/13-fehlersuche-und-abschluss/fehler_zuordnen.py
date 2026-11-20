#!/usr/bin/env python3
"""Ordnet Fehlermeldungen/Protokollzeilen einer wahrscheinlichen Ursache und einer ersten Prüfung zu (Regeln aus dem gelesenen Material: Quorum, Netzwerk, Speicher, Nested; Rest = Übungs-Erfahrungswerte, nicht bestätigt).
Aufruf: fehler_zuordnen.py [protokoll.txt]  – ohne Argument wird ein eingebautes Beispielprotokoll verwendet."""
import re, sys
REGELN = [
 (r'cluster not ready|no quorum|quorum', 'Quorum fehlt (zu viele Knoten weg)', 'pvecm status; Netzwerk/Corosync prüfen; nur im Notfall pvecm expected 1'),
 (r'KVM virtualisation configured, but not available|no support for hardware accelerated KVM', 'KVM nicht verfügbar (verschachtelte Virtualisierung aus)', 'Nested-Option am Host-Hypervisor prüfen (siehe nested_pruefen.sh)'),
 (r'storage .* is not online|unable to activate storage', 'Speicher nicht erreichbar', 'Netzwerk/Freigabe prüfen; storage.cfg und Status'),
 (r'no space left|not enough free space', 'Speicher voll', 'Belegung je Speicher, alte Backups/Snapshots prüfen'),
 (r'Name or service not known|Temporary failure in name resolution', 'Namensauflösung gestört', '/etc/hosts und DNS prüfen; Hostnamen im Cluster fix halten'),
 (r'connection timed out|no route to host', 'Netzwerk/Firewall', 'Bridge, Gateway, Firewall-Regeln prüfen'),
 (r'permission denied|403|no permission', 'Rechte fehlen', 'Benutzer, Rolle und Pfad prüfen (acl_modell.py)'),
 (r'checksum|verification failed|chunk .* missing', 'Sicherung beschädigt', 'Verify-Auftrag laufen lassen; Wiederherstellung testen'),
]
BEISPIEL = """Nov 20 10:01:11 pve1 pvedaemon[812]: VM 100 qmp command failed - KVM virtualisation configured, but not available
Nov 20 10:02:03 pve1 pmxcfs[640]: [status] notice: cluster not ready - no quorum?
Nov 20 10:03:44 pve1 pvestatd[701]: storage 'nas01' is not online
Nov 20 10:04:10 pve1 vzdump[950]: ERROR: Backup of VM 101 failed - no space left on device
Nov 20 10:05:00 pve1 pvedaemon[813]: user anna@pve: permission denied - Permission check failed
Nov 20 10:06:30 pve1 pveproxy[790]: worker exited
"""
def main():
    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else BEISPIEL
    for z in text.splitlines():
        for mu, ursache, pruef in REGELN:
            if re.search(mu, z, re.I): print('ZEILE  :', z[:100]); print('URSACHE:', ursache); print('PRÜFEN :', pruef); print(); break
        else: print('ZEILE  :', z[:100]); print('URSACHE: unbekannt (keine Regel)'); print()
main()

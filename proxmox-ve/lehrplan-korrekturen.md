# Anmerkungen zum Lehrplan P06

Beim Ausarbeiten und Testen aufgefallene Punkte. Der Lehrplan selbst wurde zusammen mit der Übungsreihe erstellt und danach **nicht** verändert.

| Nr. | Modul | Befund | Vorschlag |
|---|---|---|---|
| 1 | alle | **Labor:** Der Lehrplan beschreibt Proxmox VE auf Hyper-V mit Nested; für die Skripte diente ein Container ohne KVM und ohne Proxmox. **Keine** Proxmox-Befehle wurden ausgeführt. | Alle Module im Hyper-V-Labor erstmals durchspielen und Befund eintragen. |
| 2 | 01 | **KVM:** Im Testrechner gibt es kein `/dev/kvm`; das Skript zeigt die Auswertung „KEIN KVM“. Ob es unter Hyper-V mit Erweiterungen anders ausfällt, ist nicht geprüft. | Auf `pve1` ausführen. |
| 3 | 05 | **Device-Mapper:** `lvcreate` schlägt im Container fehl; das ist eine Eigenheit der Testumgebung. | Auf `pve1` wiederholen. |
| 4 | 06 | **VLAN:** 8021q ist im Container nicht verfügbar; VLANs wurden nicht praktisch geprüft. | In `pve1` ausprobieren. |
| 5 | 09 | **Backup-Server:** `pbs_modell.py` ist ein eigenes Modell, kein Code von Proxmox; Schonfrist und Verify-Hinweis stammen aus der gelesenen Dokumentation. | Mit echtem Backup-Server prüfen. |
| 6 | 12 | **Berechtigungen:** Die Dokumentation zu Benutzern und Rollen wurde nicht gelesen; das Modell hat erfundene Rollen. | Dokumentation lesen, Modell oder Text anpassen. |
| 7 | 14 | **Priorität:** Modul 14 ist Priorität 2; kein anderes Modul setzt es voraus. Befehlsform nicht geprüft. | Befehle gegen `qm`-Handbuch prüfen. |

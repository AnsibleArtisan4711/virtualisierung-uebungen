# Befehle und Aussagen, die nicht bestätigt sind

Prüfliste für den ersten Durchlauf: Befund und Datum eintragen, danach den Hinweis in der Übung entfernen. Legende: **Q** = gegen Quelle gelesen; **L** = real ausgeführt; **–** = weder noch.

| Modul | Aussage oder Befehl | Status | Was zu prüfen ist |
|---|---|---|---|
| alle | Alle Windows-/PowerShell-Befehle der Module | – | im Labor ausführen und Befund eintragen |
| 02 | Standardwert von `New-VM -Generation` (Learn nennt keinen) | Q (Seite gelesen, kein Wert) | `Get-VM | Select Generation` nach dem Anlegen prüfen |
| 03 | `Set-VMNetworkAdapterVlan`, Eigenschaft `PortMirroringMode` | – | `Get-Help` und Ausgabe prüfen |
| 05 | Beschreibung von Smart Paging, `-AutomaticStartAction`, `-AutomaticStopAction` | – | Learn-Seite lesen, Verhalten prüfen |
| 06 | `Checkpoint-VM`/`Restore-VMCheckpoint` mit `-SnapshotName`; Verhalten Produktions-Checkpoint nach Anwenden | Q (Learn: VM bleibt aus) | im Labor beobachten |
| 07 | Skripte `Deploy-TestVM.ps1`, `Get-HyperVReport.ps1`; Eigenschaften von `Get-ComputerInfo` (HyperV*) | – | ausführen, Syntax prüfen |
| 08 | Voraussetzungen und Einschränkungen der Nested Virtualization | – | Learn-Seite zur Nested Virtualization lesen |
| 09 | `Move-VMStorage -VHDs` allein genügend? | Q (Beispiel der Referenz) | ausprobieren |
| 09 | Aussage zu Kerberos/CredSSP ab Windows Server 2025 | – | Learn lesen |
| 10 | `-TextExtension`-Aufbau für Zertifikat, `Start-VMInitialReplication`, Regelnamen der Firewall | – | im Labor prüfen |
| 10, 12 | Hilfsskripte `Remove-ReplicaLab.ps1`, `Reset-NestedLab.ps1` | – | mit `-WhatIf` erproben |
| 11 | `.vhds` mit `-Dynamic`, Anhängen am laufenden System; Meldungen von `Test-Cluster` | – | im Labor prüfen |
| 12 | Namen der Zähler und Ereignisprotokolle, Eigenschaften von `Measure-VM` | – | im Labor ermitteln |
| 1, 3, 4, 7 | Hilfsskripte `Get-HostPrereq.ps1`, `Get-LabState.ps1` | – | ausführen |

Die Liste ist aus den Warnhinweisen der Module zusammengestellt und **nicht vollständig**; maßgeblich ist der Text der jeweiligen Übung.

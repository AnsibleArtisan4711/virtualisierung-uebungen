# Hyper-V Administration (P05)

Übungsreihe zur Administration von Hyper-V unter Windows Server (Installation, Generation-1/2-VMs, virtuelle Switches, VHDX, Speicher und CPU, Checkpoints, PowerShell, Nested Virtualization, Live-Migration, Replica, Cluster-Grundlagen, Diagnose). Zwölf Module mit je einer ausgearbeiteten Übung (Steckbrief, Lernziele, Voraussetzungen, Grundbegriffe, Aufgabe mit Zuordnung zu Lerneinheiten, Hinweise, Kontrollfragen, Musterlösung, Erweiterungen, Quellen). Gesamtumfang: 82,5 Stunden (110 Unterrichtseinheiten zu 45 Minuten, mit dem Faktor 0,75 umgerechnet).

> **Prüfstand, ehrlich:** **Es wurde nichts installiert, kein Host aufgebaut und kein Windows-Befehl ausgeführt** (Linux-Umgebung ohne PowerShell und ohne Windows). Cmdlets und Parameter wurden, soweit in den Quellen jeder Übung vermerkt, auf Microsoft Learn gelesen; Ausgaben und Fehlermeldungen sind beschrieben, nicht aufgezeichnet. Die PowerShell-Skripte (`.ps1`) wurden **nicht ausgeführt und nicht mit PowerShell syntaxgeprüft**. Offene Punkte: [`befehle-nicht-bestaetigt.md`](befehle-nicht-bestaetigt.md); Anmerkungen zum Lehrplan: [`lehrplan-korrekturen.md`](lehrplan-korrekturen.md).

## Umgebung

Ein **Hyper-V-Host** `HV-HOST01` (Windows Server 2022 oder 2025, Evaluation; mindestens 4 Kerne, 16 GB RAM, 150 GB SSD) mit den virtuellen Maschinen `VM-SRV01` (Desktop Experience), `VM-SRV02` (Server Core) und ab Modul 8 `VM-NESTED01` (verschachtelt). Switches `vSwitch-Privat-Lab` (`10.10.20.0/24`) und `vSwitch-Intern-Mgmt` (`192.168.100.0/24`), Namensraum `lab.internal`, Pfade `C:\HyperV\VMs`, `C:\HyperV\VHDs`, `C:\HyperV\Export`. Es gibt **keine** AD-Domäne. Das Labor wurde **nicht aufgebaut**.

## Module

| Nr. | Modul | Zeit | Prüfstand |
|---|---|---|---|
| 01 | [Architektur, Voraussetzungen und Installation von Hyper-V](01-architektur-und-installation/) | 6 h | Entwurf, nicht ausgeführt |
| 02 | [Virtuelle Maschinen: Generation 1 vs. Generation 2 und Basisverwaltung](02-vms-generation-1-und-2/) | 7,5 h | Entwurf, nicht ausgeführt |
| 03 | [Virtuelle Netzwerke und Hyper-V Virtual Switches](03-virtuelle-switches/) | 7,5 h | Entwurf, nicht ausgeführt |
| 04 | [Speicherverwaltung: VHD/VHDX und Differenzdatenträger](04-vhdx-und-differenzdatentraeger/) | 7,5 h | Entwurf, nicht ausgeführt |
| 05 | [Ressourcensteuerung: Virtuelle Prozessoren und Dynamischer Arbeitsspeicher](05-vcpu-und-dynamic-memory/) | 6 h | Entwurf, nicht ausgeführt |
| 06 | [Zustandssicherung mit Checkpoints (Snapshots)](06-checkpoints/) | 6 h | Entwurf, nicht ausgeführt |
| 07 | [Automatisierung und Verwaltung per PowerShell](07-powershell-automatisierung/) | 9 h | Entwurf, nicht ausgeführt |
| 08 | [Verschachtelte Virtualisierung (Nested Virtualization)](08-nested-virtualization/) | 6 h | Entwurf, nicht ausgeführt |
| 09 | [Hochverfügbarkeit I: Live-Migration und Storage Migration](09-live-migration-und-storage-migration/) (Priorität 2) | 7,5 h | Entwurf, nicht ausgeführt |
| 10 | [Disaster Recovery mit Hyper-V-Replica](10-hyper-v-replica/) (Priorität 2) | 6 h | Entwurf, nicht ausgeführt |
| 11 | [Hochverfügbarkeit II: Failover-Cluster-Grundlagen für Hyper-V](11-failover-cluster-grundlagen/) (Priorität 2) | 6 h | Entwurf, nicht ausgeführt |
| 12 | [Leistungsüberwachung, Diagnosewerkzeuge und Troubleshooting](12-performance-und-troubleshooting/) | 7,5 h | Entwurf, nicht ausgeführt |

Summe 82,5 Stunden. Priorität-2-Module: 3.

## Aufbau eines Moduls

Ordner `NN-kurzname/` mit `README.md`, der Übung `NN.1-….md` und gegebenenfalls PowerShell-Skripten (UTF-8 mit BOM, Hinweis „nicht ausgeführt“ im Kopf).

## Hinweise

- Nur im Labor ausführen; die Übungen löschen VMs, Datenträger, Zertifikate und ändern Netzwerk- und Hosteinstellungen.
- Alle Firmen, Namen und Adressen sind frei erfunden (Domänen nach RFC 2606, Adressen nach RFC 1918).
- Kennwörter und Token gehören nie in Dateien dieses Repositories; Laborwerte sind keine Zugangsdaten.

## Lizenz

- Skripte: MIT, siehe [`LICENSE`](LICENSE)
- Texte: CC BY 4.0, siehe [`LICENSE-DOCS.md`](LICENSE-DOCS.md)

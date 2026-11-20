# VMware vSphere und ESXi (P07)

Übungsreihe zu VMware vSphere und ESXi: Architektur und Grenzen des kostenlosen ESXi, Installation und Host Client, virtuelle Maschinen und .vmx, VMDK-Platten, Datastores, Netzwerk mit vSwitch und Portgruppen, Ressourcenverwaltung, Snapshots, Sicherung und Export, vCenter-Funktionen als Konzept, Rollen und Protokolle, Automatisierung, Fehlersuche. 13 Module, 106 Unterrichtseinheiten zu 45 Minuten, davon 1 Modul mit Priorität 2 (Vertiefung). Die Aufgabentexte und Kontrollfragen stammen aus dem Lehrplan P07 (Reihe „Lehrplan-Prompts“, Datei `P07-vmware-vsphere-und-esxi.md`) und sind unverändert; Hinweise, Musterlösungen und Ergänzungen sind Teil der Ausarbeitung und gekennzeichnet.

> **Prüfstand, ehrlich:** **Nicht auf ESXi ausgeführt.** Die Skripte liefen in einem Cloud-Container (Ubuntu 24.04) mit `qemu-img` und Python 3, ohne ESXi, ohne vCenter und ohne PowerShell. **Es wurden keine VMware-Befehle ausgeführt.** Aussagen zum kostenlosen ESXi stammen aus Broadcom-KB 399823 und einem Techzine-Bericht (Abruf 20.11.2026, Seite ohne Datum) und können sich ändern; alles Weitere ist Fachwissen und **nicht bestätigt**. Offene Punkte: [`befehle-nicht-bestaetigt.md`](befehle-nicht-bestaetigt.md); Anmerkungen zum Lehrplan: [`lehrplan-korrekturen.md`](lehrplan-korrekturen.md).

## Umgebung

Ein eigener ESXi-Host `esx1` (`10.7.0.11`) im isolierten Netz `10.7.0.0/24`; ob ESXi verschachtelt unter Hyper-V läuft, ist **nicht bestätigt**. Das Labor wurde **nicht** aufgebaut. Die Skripte benötigen nur Linux mit `qemu-img` und Python 3.

## Module

| Nr. | Modul | Zeit | Prüfstand |
|---|---|---|---|
| 01 | [Architektur, Produktfamilie und die Grenzen des kostenlosen ESXi](01-architektur-lizenz-und-grenzen/) | 6 h | Skript im Container ausgeführt. |
| 02 | [Installation und Host Client](02-installation-und-host-client/) | 6 h | Skript im Container ausgeführt; keine Installation. |
| 03 | [Virtuelle Maschinen und die .vmx-Datei](03-virtuelle-maschinen-und-vmx/) | 6,75 h | Skript im Container ausgeführt; keine VM gestartet. |
| 04 | [Virtuelle Platten und das VMDK-Format](04-virtuelle-platten-vmdk/) | 6 h | Skript im Container ausgeführt. |
| 05 | [Datastores und Kapazitätsplanung](05-datastores/) | 6 h | Skript im Container ausgeführt. |
| 06 | [Netzwerk: vSwitch, Portgruppen und VLANs](06-netzwerk-vswitch-und-portgruppen/) | 6,75 h | Skript im Container ausgeführt. |
| 07 | [Ressourcenverwaltung: Shares, Reservierungen und Limits](07-ressourcenverwaltung/) | 6 h | Skript im Container ausgeführt. |
| 08 | [Snapshots und Klone](08-snapshots-und-klone/) | 5,25 h | Skript im Container ausgeführt. |
| 09 | [Sicherung und Export ohne Sicherungsschnittstelle](09-sicherung-und-export/) | 6 h | Skript im Container ausgeführt. |
| 10 | [vCenter, Hochverfügbarkeit und Lastverteilung als Konzept](10-vcenter-ha-und-drs/) | 6,75 h | Modell im Container ausgeführt; kein Cluster. |
| 11 | [Benutzer, Rollen und Protokolle](11-benutzer-rollen-und-protokolle/) | 5,25 h | Modell im Container ausgeführt. |
| 12 | [Automatisierung mit PowerCLI](12-automatisierung-powercli/) (Priorität 2) | 5,25 h | Skript im Container ausgeführt; kein PowerShell. |
| 13 | [Fehlersuche und Abschluss](13-fehlersuche-und-abschluss/) | 7,5 h | Skript im Container ausgeführt. |

Summe 79,5 Stunden.

## Aufbau eines Moduls

Ordner `NN-kurzname/` mit `README.md`, der Übung `NN.1-….md` (Lernziele, Voraussetzungen, Grundbegriffe, Aufgaben, Hinweise, Kontrollfragen, einklappbare Musterlösung, Erweiterungen, Quellen), den Skripten und Beispieldaten des Moduls und einem Ordner `beispiele/` mit den echten Ausgaben der Läufe. Die Skripte der Module liegen im jeweiligen Modulordner; Python-Skripte werden über `lauf.sh` gestartet.

## Hinweise

- Die Skripte arbeiten in temporären Ordnern und starten keine VMs. Nur im Testrechner ausführen.
- Die Beispieldaten (`.vmx`, Datastores, Rollen, Pläne, Protokollzeilen) sind erfunden; Schlüssel, Rollen und PowerCLI-Befehle stammen aus Fachwissen und sind nicht bestätigt.
- Der kostenlose ESXi hat laut gelesener Quelle Einschränkungen (u. a. kein vCenter, kein vMotion/DRS/HA); Stand 20.11.2026, bitte vor Einsatz beim Hersteller prüfen. Keine Lizenzberatung.

## Lizenz

- Skripte: MIT, siehe [`LICENSE`](LICENSE)
- Texte: CC BY 4.0, siehe [`LICENSE-DOCS.md`](LICENSE-DOCS.md)

*Lizenz: Text CC BY 4.0, Skripte MIT, siehe `LICENSE-DOCS.md` und `LICENSE` im Kursordner. Alle Personen, Firmen, Zahlen und Termine sind frei erfunden. Windows und Windows Server sind Marken der Microsoft Corporation; dieses Dokument steht in keiner Verbindung zu Microsoft.*

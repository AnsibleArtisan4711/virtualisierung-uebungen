# Proxmox VE (P06)

Übungsreihe zu Proxmox VE: Architektur und Nested-Installation, Weboberfläche und Speicherkonfiguration, virtuelle Maschinen, LXC-Container, Speicher, Netzwerk und Bridges, Vorlagen und Abbild-Formate, Snapshots, Datensicherung und Backup-Server, Cluster und Hochverfügbarkeit, Migration, Benutzer und Berechtigungen, Fehlersuche, Automatisierung. 14 Module, 115 Unterrichtseinheiten zu 45 Minuten, davon 1 Modul mit Priorität 2 (Vertiefung). Die Aufgabentexte und Kontrollfragen stammen aus dem Lehrplan P06 (Reihe „Lehrplan-Prompts“, Datei `P06-proxmox-ve.md`) und sind unverändert; Hinweise, Musterlösungen und Ergänzungen sind Teil der Ausarbeitung und gekennzeichnet.

> **Prüfstand, ehrlich:** **Nicht auf Proxmox VE ausgeführt.** Die Skripte liefen in einem Cloud-Container (Ubuntu 24.04) ohne KVM und ohne Proxmox. Sie zeigen Konzepte mit `qemu-img`, Netzwerk-Namespaces, Bridges, LVM auf Loop-Geräten sowie Python-Modellen (Speicherprüfung, Chunk-Speicher, Quorum, Rechte, Fehlerzuordnung). **Es wurden keine Proxmox-Befehle ausgeführt.** Aussagen zu Proxmox VE stammen aus der gelesenen Dokumentation (Abruf 20.11.2026, siehe Lehrplan, Quellen) oder sind Fachwissen und **nicht bestätigt**. Offene Punkte: [`befehle-nicht-bestaetigt.md`](befehle-nicht-bestaetigt.md); Anmerkungen zum Lehrplan: [`lehrplan-korrekturen.md`](lehrplan-korrekturen.md).

## Umgebung

Proxmox VE unter **Hyper-V** mit verschachtelter Virtualisierung: `pve1` (`10.6.0.11`), `pve2`, `pve3` für Cluster und Migration, optional `pbs1` am privaten Switch `Lab-PVE` (`10.6.0.0/24`). Das Labor wurde **nicht** aufgebaut. Die Skripte benötigen nur Linux mit `qemu-img`, `ip`, `lvm2` und Python 3.

## Module

| Nr. | Modul | Zeit | Prüfstand |
|---|---|---|---|
| 01 | [Architektur, Installation und verschachtelte Virtualisierung](01-architektur-und-installation/) | 6 h | Skript im Container ausgeführt; Installation nicht ausgeführt. |
| 02 | [Weboberfläche, Shell und die Speicherkonfiguration](02-oberflaeche-shell-und-speicherkonfiguration/) | 6 h | Skript im Container ausgeführt; Oberfläche nicht geprüft. |
| 03 | [Virtuelle Maschinen mit KVM](03-virtuelle-maschinen/) | 6 h | Skript im Container ausgeführt; keine VM gestartet. |
| 04 | [Container mit LXC](04-container-mit-lxc/) | 6 h | Skript im Container ausgeführt; kein LXC-Container erstellt. |
| 05 | [Speicher: Verzeichnis, LVM, ZFS, NFS und Ceph](05-speicher/) | 6,75 h | Skript im Container ausgeführt (LVM teilweise). |
| 06 | [Netzwerk: Linux-Bridges und VLANs](06-netzwerk-und-bridges/) | 6,75 h | Skripte im Container ausgeführt; VLAN nicht geprüft. |
| 07 | [Vorlagen, Klone und Abbild-Formate](07-vorlagen-klone-und-images/) | 5,25 h | Skript im Container ausgeführt; keine VM gestartet. |
| 08 | [Snapshots](08-snapshots/) | 5,25 h | Skript im Container ausgeführt. |
| 09 | [Datensicherung und Proxmox Backup Server](09-datensicherung-und-backup-server/) | 6,75 h | Modell im Container ausgeführt; Backup-Server nicht geprüft. |
| 10 | [Cluster, Quorum und Hochverfügbarkeit](10-cluster-und-hochverfuegbarkeit/) | 6,75 h | Skript im Container ausgeführt; kein Cluster aufgebaut. |
| 11 | [Migration: Live-Migration und Wechsel von anderen Hypervisoren](11-migration/) | 6 h | Skript im Container ausgeführt; Migration nicht ausgeführt. |
| 12 | [Benutzer, Rollen und Berechtigungen](12-benutzer-und-berechtigungen/) | 6 h | Modell im Container ausgeführt; Proxmox-Rechte nicht geprüft. |
| 13 | [Fehlersuche und Abschluss](13-fehlersuche-und-abschluss/) | 7,5 h | Skript im Container ausgeführt. |
| 14 | [Automatisierung mit CLI und API](14-automatisierung-cli-und-api/) (Priorität 2) | 5,25 h | Skript im Container ausgeführt; keine Befehle auf Proxmox. |

Summe 86,25 Stunden.

## Aufbau eines Moduls

Ordner `NN-kurzname/` mit `README.md`, der Übung `NN.1-….md` (Lernziele, Voraussetzungen, Grundbegriffe, Aufgaben, Hinweise, Kontrollfragen, einklappbare Musterlösung, Erweiterungen, Quellen), den Skripten und Beispieldaten des Moduls und einem Ordner `beispiele/` mit den echten Ausgaben der Läufe. Die Skripte der Module liegen im jeweiligen Modulordner; Python-Skripte werden über `lauf.sh` gestartet.

## Hinweise

- Die Skripte arbeiten in temporären Ordnern und Namespaces und starten keine VMs; `lvm_demo.sh` und `bridge_demo.sh` verändern vorübergehend Loop-Geräte bzw. Netzwerk-Namespaces und räumen auf. Nur im Testrechner als root ausführen.
- Die Beispieldaten (Konfigurationen, Protokollzeilen, Rollen, Pläne) sind erfunden; die Rollen in Modul 12 entsprechen nicht den echten Rollen.
- Proxmox-VE-Befehle (`qm`, `pct`, `pvesm`, `pvecm`, `vzdump`) sind Fachwissen bzw. aus der Dokumentation und wurden nicht ausgeführt.

## Lizenz

- Skripte: MIT, siehe [`LICENSE`](LICENSE)
- Texte: CC BY 4.0, siehe [`LICENSE-DOCS.md`](LICENSE-DOCS.md)

*Lizenz: Text CC BY 4.0, Skripte MIT, siehe `LICENSE-DOCS.md` und `LICENSE` im Kursordner. Alle Personen, Firmen, Zahlen und Termine sind frei erfunden. Windows und Windows Server sind Marken der Microsoft Corporation; dieses Dokument steht in keiner Verbindung zu Microsoft.*

# Failover-Clustering und Hochverfügbarkeit (P60)

Übungsreihe zu Failover-Clustering und Hochverfügbarkeit: Verfügbarkeit und Ausfallkonzepte, Clusteraufbau, Quorum und Zeugen, gemeinsamer Speicher und Cluster Shared Volumes, hochverfügbare VMs und Live-Migration, Hyper-V Replica, Cluster-aware Updating und Überwachung sowie Fehlersuche und Ausfalltests. 8 Module, 100 Unterrichtseinheiten zu 45 Minuten, davon 1 Modul mit Priorität 2 (Vertiefung). Python-Modelle mit PowerShell-Textdateien; nichts davon wurde auf Windows Server ausgeführt. Die Aufgabentexte und Kontrollfragen stammen aus dem Lehrplan P60 (Reihe „Lehrplan-Prompts“, Datei `P60-failover-clustering-und-hochverfuegbarkeit.md`) und sind unverändert; Hinweise, Musterlösungen und Ergänzungen sind Teil der Ausarbeitung und gekennzeichnet.

> **Prüfstand, ehrlich:** **Nur Python-Modelle ausgeführt, nicht Windows Server.** Die Ausgaben in den Ordnern `beispiele/` stammen von vereinfachten Modellen mit erfundenen Werten (Python 3 im Cloud-Container). **Failover-Cluster, Hyper-V und PowerShell wurden nicht ausgeführt**: Die Befehle sind Fachwissen und nicht bestätigt. Offene Punkte: [`befehle-nicht-bestaetigt.md`](befehle-nicht-bestaetigt.md); Anmerkungen zum Lehrplan: [`lehrplan-korrekturen.md`](lehrplan-korrekturen.md).

## Umgebung

Zwei Hyper-V-Hosts, ein Domänencontroller und eine Speicher-VM oder ein iSCSI-Ziel (Lehrplan) am privaten Switch `Lab-Cluster` (`10.60.0.0/24`). Das Labor wurde **nicht** aufgebaut. Die Python-Modelle laufen auf jedem Rechner mit Python 3.

## Module

| Nr. | Modul | Zeit | Prüfstand |
|---|---|---|---|
| 01 | [Hochverfügbarkeit und Ausfallkonzepte](01-hochverfuegbarkeit-und-ausfallkonzepte/) | 9 h | Modell ausgeführt. |
| 02 | [Failover-Cluster aufbauen](02-failover-cluster-aufbauen/) | 10,5 h | Modell ausgeführt; Cluster nicht aufgebaut. |
| 03 | [Quorum und Zeugen](03-quorum-und-zeugen/) | 10,5 h | Modell ausgeführt. |
| 04 | [Gemeinsamer Speicher und Cluster Shared Volumes](04-gemeinsamer-speicher-und-csv/) | 9 h | Modell ausgeführt. |
| 05 | [Hochverfügbare VMs und Live-Migration](05-hochverfuegbare-vms-und-live-migration/) | 10,5 h | Modell ausgeführt. |
| 06 | [Hyper-V Replica](06-hyper-v-replica/) (Priorität 2) | 7,5 h | Modell ausgeführt. |
| 07 | [Cluster-aware Updating und Überwachung](07-cluster-aware-updating-und-ueberwachung/) | 9 h | Modell ausgeführt. |
| 08 | [Fehlersuche und Ausfalltests](08-fehlersuche-und-ausfalltests/) | 9 h | Modell ausgeführt. |

Summe 75 Stunden.

## Aufbau eines Moduls

Ordner `NN-kurzname/` mit `README.md`, der Übung `NN.1-….md` (Lernziele, Voraussetzungen, Grundbegriffe, Aufgaben, Hinweise, Kontrollfragen, einklappbare Musterlösung, Erweiterungen, Quellen), den Skripten und Beispieldaten des Moduls und einem Ordner `beispiele/` mit den echten Ausgaben der Läufe. Die Skripte der Module liegen im jeweiligen Modulordner.

## Hinweise

- Die Python-Modelle verändern nichts am System.
- Alle Namen, Adressen (`10.60.0.0/24`) und Werte sind erfunden.
- Die PowerShell-Textdateien wurden nicht ausgeführt und nicht gegen die Dokumentation geprüft; sie gehören nur in ein Testlabor.

## Lizenz

- Skripte: MIT, siehe [`LICENSE`](LICENSE)
- Texte: CC BY 4.0, siehe [`LICENSE-DOCS.md`](LICENSE-DOCS.md)

*Lizenz: Text CC BY 4.0, Skripte MIT, siehe `LICENSE-DOCS.md` und `LICENSE` im Kursordner. Alle Personen, Firmen, Zahlen und Termine sind frei erfunden. Windows und Windows Server sind Marken der Microsoft Corporation; dieses Dokument steht in keiner Verbindung zu Microsoft.*

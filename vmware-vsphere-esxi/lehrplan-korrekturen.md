# Anmerkungen zum Lehrplan P07

Beim Ausarbeiten und Testen aufgefallene Punkte. Der Lehrplan selbst wurde zusammen mit der Übungsreihe erstellt und danach **nicht** verändert.

| Nr. | Modul | Befund | Vorschlag |
|---|---|---|---|
| 1 | alle | **Labor:** Der Lehrplan beschreibt einen eigenen ESXi-Host; ob ESXi verschachtelt unter Hyper-V läuft, ist **nicht bestätigt**. Die Skripte liefen in einem Container ohne ESXi, ohne vCenter und ohne PowerShell. | Auf geeigneter Hardware durchspielen und Befund eintragen. |
| 2 | 01 | **Lizenzstand:** Die Angaben zum kostenlosen ESXi stammen aus KB 399823 (gelesen 20.11.2026, Seite ohne Datum) und Techzine; sie können sich ändern. Berichte zu geänderten Mindestkernzahlen sind nicht bestätigt und wurden nicht verwendet. | Vor jedem Kurs erneut beim Hersteller prüfen und Stand eintragen. |
| 3 | 02 | **Richtwerte:** 2 Kerne, 8 GB, 40 GB sind eigene Annahmen, keine Herstellerangaben. | Mit Hardware-Kompatibilitätsliste des Herstellers abgleichen. |
| 4 | 07 | **Verfahren:** Die Verteilung nach Shares ist vereinfacht und kein ESXi-Algorithmus. | Dokumentation lesen, Beschreibung ggf. anpassen. |
| 5 | 10 | **Konzeptmodul:** Cluster-Funktionen sind beim kostenlosen ESXi nicht verfügbar; das Modul ist rein konzeptionell. | Bei Bedarf mit vCenter-Testlizenz ergänzen (nicht geprüft). |
| 6 | 12 | **Priorität:** Modul 12 ist Priorität 2; kein anderes Modul setzt es voraus. Befehlsform nicht geprüft. | PowerCLI-Dokumentation lesen. |

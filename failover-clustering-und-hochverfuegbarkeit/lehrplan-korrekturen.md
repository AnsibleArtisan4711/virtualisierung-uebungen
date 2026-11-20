# Anmerkungen zum Lehrplan P60

Beim Ausarbeiten aufgefallene Punkte. Der Lehrplan selbst wurde zusammen mit der Übungsreihe erstellt und danach **nicht** verändert.

| Nr. | Modul | Befund | Vorschlag |
|---|---|---|---|
| 1 | alle | **Ausführung:** Ausgeführt wurden nur die Python-Modelle (Cloud-Container, Python 3). Windows Server, Failover-Cluster, Hyper-V und PowerShell wurden **nicht** verwendet; alle fachlichen Aussagen und Cmdlets sind Fachwissen und **nicht bestätigt**. | Auf den Hyper-V-Hosts nachvollziehen. |
| 2 | alle | **Quellen:** Die Dokumentation von Windows Server, Failover Clustering und Hyper-V wurde nicht gelesen. Versions-, Lizenz- und Supportstände sind mit Stand zu prüfen. | Quellen lesen und eintragen. |
| 3 | 03 | **Quorum-Modell:** Das Modell kennt nur eine einfache statische Mehrheit; dynamisches Quorum und Zeugenverhalten sind nicht abgebildet. | In der Dokumentation der eingesetzten Version prüfen. |
| 4 | 05 | **Platzierung:** Das Modell berücksichtigt nur RAM und First-Fit; die Reihenfolge und Platzierung im echten Cluster hängen von Prioritäten und Regeln ab. | Im Labor beobachten. |
| 5 | 06 | **Priorität:** Modul 6 ist Priorität 2; kein anderes Modul setzt es voraus. | Bei Zeitmangel entfallen lassen. |

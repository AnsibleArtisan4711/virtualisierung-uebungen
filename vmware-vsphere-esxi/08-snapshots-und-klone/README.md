# 08 Snapshots

Übung **08.1** (Priorität 1). Geschätzte Zeit: 4 bis 6 Stunden (Schätzung; Lehrplan: 7 UE zu 45 Minuten = 5,25 Stunden).

> Skript im Container ausgeführt.

| Datei | Zweck |
|---|---|
| `08.1-snapshots-und-klone.md` | Die Übung mit Aufgaben, Kontrollfragen und Musterlösung |
| `snapshot_kette.sh` | Snapshot-Kette als Differenzabbilder (qcow2-Overlays) nachgebildet: jeder „Snapshot“ legt ein neues Differenzabbild an, Schreibzugriffe landen im obersten; Zusammenführen (commit) bündelt sie wieder. |
| `beispiele/snapshot_kette.ausgabe.txt` | Echte Ausgabe des Laufs von `snapshot_kette` |

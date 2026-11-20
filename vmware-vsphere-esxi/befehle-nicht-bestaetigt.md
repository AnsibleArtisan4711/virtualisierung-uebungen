# Befehle und Aussagen, die nicht bestätigt sind

Prüfliste für den ersten Durchlauf in den Hyper-V-VMs: Befund und Datum eintragen, danach den Hinweis in der Übung entfernen. Legende: **Q** = gegen Quelle gelesen; **L** = im Labor (Container) ausgeführt; **–** = weder noch.

| Modul | Befehl oder Aussage | Status | Nächster Schritt |
|---|---|---|---|
| alle | Aufbau des Labors: eigener ESXi-Host `esx1` (nicht bestätigt unter Hyper-V), isoliertes Netz `10.7.0.0/24` | – | laut Lehrplan aufbauen und prüfen |
| 01 | `gratis_grenzen_pruefen.py` (Grenzen aus Broadcom-KB 399823, gelesen 20.11.2026, Seite ohne Datum) | L; Quelle gelesen, Stand unsicher | Grenzen beim Hersteller erneut prüfen |
| 02 | `voraussetzungen_pruefen.sh` (Richtwerte 2 Kerne, 8 GB, 40 GB sind eigene Annahmen) | L | auf dem vorgesehenen Gerät ausführen; Hardware-Kompatibilität beim Hersteller prüfen |
| 03 | `vmx_pruefen.py`, `web01.vmx`, `alt01.vmx` (erfunden; Schlüssel aus Fachwissen) | L; ESXi – | mit echter .vmx vergleichen |
| 04 | `vmdk_demo.sh` (qemu-img: monolithicSparse, monolithicFlat, streamOptimized) | L (qemu-img 8.2.2); ESXi – | mit einer echten VMDK vom ESXi vergleichen |
| 05 | `datastore_rechner.py` (erfundene Werte) | L | mit echten Datastores rechnen |
| 06 | `portgruppen_pruefen.py` (Modell mit erfundener Konfiguration) | L | mit echtem vSwitch vergleichen |
| 07 | `ressourcen_rechner.py` (stark vereinfachtes Verfahren, nicht der ESXi-Algorithmus) | L | Dokumentation zu Reservierung/Limit/Shares lesen |
| 08 | `snapshot_kette.sh` (qcow2-Differenzabbilder als Analogon) | L | mit echten Snapshots auf `esx1` vergleichen |
| 09 | `export_import.sh` (Export mit Prüfsumme an einem Plattenabbild) | L | echtes OVF-Export/Import ausprobieren |
| 10 | `ha_modell.py` (Modell; kostenloser ESXi hat kein HA/DRS/vCenter) | L (Rechnung); Cluster – | nur mit vCenter und passender Lizenz |
| 11 | `rollen_modell.py` (erfundenes Rollenmodell) | L; ESXi – | Dokumentation zu Rollen lesen |
| 12 | `plan_zu_powercli.py` (Befehle nur als Text) | L (Text); PowerShell – | Befehle gegen die PowerCLI-Dokumentation prüfen |
| 13 | `fehler_zuordnen.py` (Erfahrungswerte, erfundene Zeilen) | L | mit echten Protokollen testen |

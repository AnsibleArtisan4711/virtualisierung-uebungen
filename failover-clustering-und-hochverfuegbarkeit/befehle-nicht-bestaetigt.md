# Befehle und Aussagen, die nicht bestätigt sind

Prüfliste für den ersten Durchlauf in den Hyper-V-VMs: Befund und Datum eintragen, danach den Hinweis in der Übung entfernen. Legende: **Q** = gegen Quelle gelesen; **L** = im Labor (Container) ausgeführt; **–** = weder noch.

| Modul | Befehl oder Aussage | Status | Nächster Schritt |
|---|---|---|---|
| alle | Aufbau des Hyper-V-Labors (privater Switch `Lab-Cluster`, `hv01`, `hv02`, `dc01`, `san01`) | – | laut Lehrplan aufbauen und prüfen |
| 01 | `verfuegbarkeit.py` | Modell ausgeführt | Werte mit Herstellerangaben abgleichen |
| 02 | `voraussetzungen.py`; `beispiel_powershell.txt` (`Install-WindowsFeature`, `Test-Cluster`, `New-Cluster`) | Modell ausgeführt; PowerShell: nicht ausgeführt | auf `hv01`/`hv02` ausführen |
| 03 | `quorum.py`; `beispiel_powershell.txt` (`Get-ClusterQuorum`, `Set-ClusterQuorum`) | Modell ausgeführt (einfache Mehrheit); PowerShell: nicht ausgeführt | dynamisches Quorum in der Dokumentation prüfen |
| 04 | `csv_modell.py`; `beispiel_powershell.txt` (`Add-ClusterDisk`, `Add-ClusterSharedVolume`, `Get-ClusterSharedVolume`) | Modell ausgeführt; PowerShell: nicht ausgeführt | auf dem Cluster ausführen |
| 05 | `failover_sim.py`; `beispiel_powershell.txt` (`Add-ClusterVirtualMachineRole`, `Move-ClusterVirtualMachineRole`) | Modell ausgeführt (nur RAM); PowerShell: nicht ausgeführt | Ausfall im Labor nachstellen |
| 06 | `replica_rpo.py`; `beispiel_powershell.txt` (`Enable-VMReplication`, `Start-VMInitialReplication`, `Get-VMReplication`) | Modell ausgeführt; PowerShell: nicht ausgeführt | mit zwei Hosts testen |
| 07 | `cau_plan.py`; `beispiel_powershell.txt` (`Add-CauClusterRole`, `Invoke-CauScan`, `Invoke-CauRun`) | Modell ausgeführt; PowerShell: nicht ausgeführt | im Labor testen |
| 08 | `ausfalltest_plan.py`; `beispiel_powershell.txt` (`Get-ClusterNode`, `Get-ClusterGroup`, `Get-ClusterLog`, `Test-Cluster`) | Modell ausgeführt; PowerShell: nicht ausgeführt | Ausfalltests im Labor durchführen |

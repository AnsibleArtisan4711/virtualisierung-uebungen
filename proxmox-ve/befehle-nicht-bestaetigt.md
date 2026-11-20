# Befehle und Aussagen, die nicht bestätigt sind

Prüfliste für den ersten Durchlauf in den Hyper-V-VMs: Befund und Datum eintragen, danach den Hinweis in der Übung entfernen. Legende: **Q** = gegen Quelle gelesen; **L** = im Labor (Container) ausgeführt; **–** = weder noch.

| Modul | Befehl oder Aussage | Status | Nächster Schritt |
|---|---|---|---|
| alle | Aufbau des Labors: Hyper-V mit verschachtelter Virtualisierung, privater Switch `Lab-PVE`, `pve1` bis `pve3`, optional `pbs1` | – | laut Lehrplan aufbauen und prüfen |
| 01 | `nested_pruefen.sh` (vmx/svm, `/dev/kvm`, Module); Hyper-V-Befehl `Set-VMProcessor -ExposeVirtualizationExtensions $true` | L (Container ohne KVM: „KEIN KVM“); Hyper-V – (aus Microsoft-Dokumentation gelesen) | auf `pve1` wiederholen |
| 02 | `storage_pruefen.py` (Tabelle der Speichertypen aus der Dokumentation, Beispielkonfiguration erfunden) | L | mit eigener `storage.cfg` prüfen |
| 03 | `vm_conf_pruefen.py`, `100.conf` (erfunden); Gerätemodelle und Gast-Agent | L; Proxmox – | mit echter VM-Konfiguration vergleichen |
| 04 | `namespaces_demo.sh` (`unshare`); LXC und `pct` | L (nur `unshare`); LXC – | auf `pve1` einen Container anlegen |
| 05 | `lvm_demo.sh` (`pvcreate`, `vgcreate`; `lvcreate` scheitert im Container) | L teilweise | auf `pve1` mit echten Platten wiederholen; ZFS/NFS/Ceph prüfen |
| 06 | `bridge_demo.sh` (Bridge, Namespaces, veth), `interfaces_pruefen.py`; VLAN-aware Bridge, `ifreload -a` | L; VLAN – (8021q im Container nicht verfügbar) | auf `pve1` ausprobieren |
| 07 | `qemu_img_demo.sh` (raw, qcow2, vmdk, vhdx, Overlays); `qm clone`/`qm template` | L (qemu-img 8.2.2); Proxmox – | auf `pve1` klonen und Platz messen |
| 08 | `snapshot_demo.sh` (interne qcow2-Snapshots) | L | mit Proxmox-Snapshots auf `pve1` vergleichen |
| 09 | `pbs_modell.py` (eigenes vereinfachtes Modell); Prune, GC, Verify (Dokumentation gelesen) | L (Modell); Backup-Server – | `pbs1` einrichten, echte Sicherung und Wiederherstellung |
| 10 | `quorum_rechner.py`; `pvecm`-Befehle und Ports aus der Dokumentation | L (Rechnung); Cluster – | Cluster aus `pve1` bis `pve3` bauen |
| 11 | `migration_vhdx.sh` (VHDX → qcow2/vmdk, Vergleich); Live-Migration | L; Migration – | Windows-VM migrieren und Start prüfen |
| 12 | `acl_modell.py` (erfundene Rollen); Benutzer, Rollen, Pfade in Proxmox | L (Modell); Proxmox – (nicht gelesen) | Dokumentation lesen und Modell angleichen |
| 13 | `fehler_zuordnen.py` (Regeln aus Dokumentation und Erfahrung, Beispielzeilen erfunden) | L | mit echten Protokollen testen |
| 14 | `plan_zu_befehlen.py` (Befehle nur als Text) | L (nur Textausgabe) | Befehlsform gegen `qm`-Handbuch prüfen |

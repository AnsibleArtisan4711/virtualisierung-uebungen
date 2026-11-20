#!/usr/bin/env bash
# Snapshots auf Abbildebene mit qemu-img: interne qcow2-Snapshots anlegen, Daten ändern, zurückrollen, löschen. Vorbild für „Snapshot erstellen/zurückrollen“ bei Proxmox-VMs auf qcow2-Speicher (Dokumentation: Snapshots auf Directory/NFS/CIFS nur mit qcow2).
# Benötigt: qemu-img, qemu-io. Es wird KEINE VM gestartet. Arbeitet in einem temporären Ordner.
set -eu
T=$(mktemp -d /tmp/p06-snap.XXXX); trap 'rm -rf $T' EXIT; cd $T
rd() { qemu-io -f qcow2 -c "read -P $2 0 4k" $1 2>&1 | head -1 | sed 's/^/  /'; }
echo "## 1. Abbild mit bekanntem Inhalt (Muster 0xaa)"
qemu-img create -q -f qcow2 vm.qcow2 32M; qemu-io -f qcow2 -c 'write -P 0xaa 0 4k' vm.qcow2 >/dev/null; rd vm.qcow2 0xaa
echo; echo "## 2. Snapshot „vor-update“ anlegen und Inhalt ändern (Muster 0xbb)"
qemu-img snapshot -c vor-update vm.qcow2; qemu-io -f qcow2 -c 'write -P 0xbb 0 4k' vm.qcow2 >/dev/null
rd vm.qcow2 0xbb; qemu-img snapshot -l vm.qcow2 | sed 's/^/  /' | cut -c1-70
echo; echo "## 3. Zurückrollen (-a): Inhalt ist wieder das alte Muster"
qemu-img snapshot -a vor-update vm.qcow2; rd vm.qcow2 0xaa
echo; echo "## 4. Snapshot löschen (-d) und Prüfung"
qemu-img snapshot -d vor-update vm.qcow2; qemu-img snapshot -l vm.qcow2 | sed 's/^/  /'; echo "  (keine Snapshots mehr)"; qemu-img check vm.qcow2 | head -1 | sed 's/^/  /'
echo; echo "## 5. Beobachtung zur Größe: jede Änderung nach einem Snapshot belegt zusätzlichen Platz"
qemu-img snapshot -c a vm.qcow2; qemu-io -f qcow2 -c 'write -P 0x01 0 8M' vm.qcow2 >/dev/null; printf '  belegt nach 8 MB Änderung mit Snapshot: %s\n' "$(qemu-img info vm.qcow2 | awk -F': ' '/^disk size/ {print $2; exit}')"

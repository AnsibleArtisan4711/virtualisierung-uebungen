#!/usr/bin/env bash
# Platten einer Hyper-V-VM (VHDX) für Proxmox VE oder VMware (VMDK) umwandeln – nur das Abbild, ohne VM. Prüft Ergebnis und Größen.
# Benötigt: qemu-img. Temporärer Ordner, es wird nichts gestartet. NICHT geprüft: ob ein Gast nach der Umwandlung bootet (Treiber, UEFI/BIOS, Controller).
set -eu
T=$(mktemp -d /tmp/p06-mig.XXXX); trap 'rm -rf $T' EXIT; cd $T
gr() { qemu-img info "$1" | awk -F': ' '/^disk size/ {print $2; exit}'; }
echo "## 1. Hyper-V-Platte (VHDX, 128 MB virtuell, 6 MB Daten) vorbereiten"
qemu-img create -q -f vhdx -o subformat=dynamic hv.vhdx 128M; qemu-io -f vhdx -c 'write -P 0x42 0 6M' hv.vhdx >/dev/null
echo "  hv.vhdx belegt: $(gr hv.vhdx)"
echo; echo "## 2. Nach qcow2 (Proxmox VE, importierbar auf Dateispeicher) und nach VMDK (VMware)"
qemu-img convert -f vhdx -O qcow2 hv.vhdx pve.qcow2; qemu-img convert -f vhdx -O vmdk -o subformat=monolithicSparse hv.vhdx vm.vmdk
echo "  pve.qcow2 belegt: $(gr pve.qcow2)"; echo "  vm.vmdk   belegt: $(gr vm.vmdk)"
echo; echo "## 3. Inhalt vergleichen"
qemu-img compare -f vhdx -F qcow2 hv.vhdx pve.qcow2 | sed 's/^/  qcow2: /'; qemu-img compare -f vhdx -F vmdk hv.vhdx vm.vmdk | sed 's/^/  vmdk:  /'
echo; echo "## 4. Eigenschaften der Ergebnisse"
for f in pve.qcow2 vm.vmdk; do qemu-img info $f | awk -v f=$f '/file format|virtual size/ {printf "  %s: %s %s\n", f, $1" "$2, $3" "$4}'; done
echo; echo "## 5. Checkliste für eine echte Migration (Fachwissen, nicht bestätigt)"
printf '  - Quell-VM sauber herunterfahren, Schnellstart/Ruhezustand von Windows aus\n  - Treiber (virtio bzw. VMware-Tools) vor dem Wechsel bereitstellen\n  - Firmware-Typ (BIOS/UEFI) in der Ziel-VM gleich einstellen\n  - Netzwerkkarte neu zuordnen, MAC/IP prüfen\n  - Test auf Kopie, Rückweg über die Quell-VM behalten\n'

#!/usr/bin/env bash
# LVM-Grundlagen mit einer Loop-Datei: Physical Volume und Volume Group lassen sich anlegen; Logical Volumes (und damit LVM-thin) brauchen den Device-Mapper des Kernels.
# Benötigt: lvm2, losetup, root. Im Testlabor (Cloud-Container) fehlt der Device-Mapper: der Schritt 3 schlägt dort fehl und wird hier absichtlich so gezeigt.
set -u
IMG=/tmp/p06-lvm.img; VG=p06vg
cleanup() { vgremove -qf $VG >/dev/null 2>&1; [ -n "${L:-}" ] && { pvremove -qf "$L" >/dev/null 2>&1; losetup -d "$L" 2>/dev/null; }; rm -f $IMG; }
trap cleanup EXIT
echo "## 1. Loop-Gerät als Ersatz für eine Platte (64 MB)"
dd if=/dev/zero of=$IMG bs=1M count=64 status=none; L=$(losetup -f --show $IMG); echo "Gerät: $L"
echo; echo "## 2. Physical Volume und Volume Group anlegen"
pvcreate -q "$L" 2>&1 | sed 's/^ *//'; vgcreate -q $VG "$L" 2>&1 | sed 's/^ *//'
vgs --noheadings -o vg_name,vg_size,vg_free,pv_count $VG 2>&1 | sed 's/^ */  /'
echo; echo "## 3. Logical Volume anlegen (braucht den Device-Mapper)"
lvcreate -q -L 8M -n lv1 $VG 2>&1 | sed 's/^ *//' | head -4
echo "Rückgabewert: ${PIPESTATUS[0]}"
echo; echo "## 4. Folgerung"
echo "Proxmox VE legt für VM-Platten auf LVM je ein Logical Volume an (Fachwissen, nicht bestätigt); ohne Device-Mapper wäre das hier nicht möglich. Die Metadaten-Schritte (PV, VG) funktionieren auch ohne."

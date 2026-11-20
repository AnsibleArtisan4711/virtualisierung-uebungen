#!/usr/bin/env bash
# Datenträgerabbilder umwandeln und mit Overlays arbeiten (qemu-img): raw, qcow2, VMDK, VHDX; Kopie auf Basisabbild (Backing File) als Vorbild eines „verknüpften Klons“.
# Benötigt: qemu-img. Arbeitet in einem temporären Ordner und räumt auf. Es wird KEINE VM gestartet.
set -eu
T=$(mktemp -d /tmp/p06-img.XXXX); trap 'rm -rf $T' EXIT; cd $T
gr() { qemu-img info "$1" | awk -F': ' '/^disk size/ {print $2; exit}'; }
bf() { qemu-img info "$1" | awk -F': ' '/^backing file:/ {print $2; exit}'; }
echo "## 1. Leeres Abbild in vier Formaten anlegen (je 64 MB virtuell)"
for f in raw qcow2 vmdk vhdx; do qemu-img create -q -f $f disk.$f 64M; done
for f in raw qcow2 vmdk vhdx; do printf '  %-6s Format: %-6s belegt: %s\n' disk.$f "$(qemu-img info disk.$f | awk '/file format/ {print $3}')" "$(gr disk.$f)"; done
echo; echo "## 2. Daten schreiben und in andere Formate umwandeln"
dd if=/dev/urandom of=daten.bin bs=1M count=8 status=none
qemu-io -f raw -c 'write -P 0x5a 0 8M' disk.raw >/dev/null
qemu-img convert -f raw -O qcow2 disk.raw conv.qcow2; qemu-img convert -f raw -O vmdk -o subformat=streamOptimized disk.raw conv.vmdk; qemu-img convert -f raw -O vhdx disk.raw conv.vhdx
for f in qcow2 vmdk vhdx; do printf '  conv.%-6s belegt: %s\n' $f "$(gr conv.$f)"; done
echo; echo "## 3. Inhalt prüfen: die umgewandelten Abbilder enthalten dieselben Daten wie das Original"
for f in qcow2 vmdk vhdx; do qemu-img compare -f raw -F $f disk.raw conv.$f | sed "s/^/  conv.$f: /"; done
echo; echo "## 4. Basisabbild und Overlay (Backing File)"
qemu-img create -q -f qcow2 -b conv.qcow2 -F qcow2 klon1.qcow2; qemu-img create -q -f qcow2 -b conv.qcow2 -F qcow2 klon2.qcow2
for k in klon1 klon2; do printf '  %s belegt: %s, Basis: %s\n' $k "$(gr $k.qcow2)" "$(bf $k.qcow2)"; done
qemu-io -f qcow2 -c 'write -P 0x11 0 1M' klon1.qcow2 >/dev/null
echo "Nach 1 MB Schreiben in klon1:"; printf '  klon1 belegt: %s\n' "$(gr klon1.qcow2)"
echo; echo "## 5. Overlay mit der Basis zusammenführen (vollständiger Klon)"
qemu-img convert -O qcow2 klon1.qcow2 voll1.qcow2; printf '  voll1 belegt: %s, Basis: %s\n' "$(gr voll1.qcow2)" "$(b=$(bf voll1.qcow2); echo ${b:-keine})"

#!/usr/bin/env bash
# Snapshot-Kette als Differenzabbilder (qcow2-Overlays) nachgebildet: jeder „Snapshot“ legt ein neues Differenzabbild an, Schreibzugriffe landen im obersten; Zusammenführen (commit) bündelt sie wieder.
# Das ist ein ANALOGON zu den Differenzplatten von VMware (Fachwissen), kein ESXi-Verhalten. Kein ESXi beteiligt.
set -eu
T=$(mktemp -d /tmp/p07-snap.XXXX); trap 'rm -rf $T' EXIT; cd $T
gr() { qemu-img info "$1" | awk -F': ' '/^disk size/ {print $2; exit}'; }
qemu-img create -q -f qcow2 basis.qcow2 64M; qemu-io -f qcow2 -c 'write -P 0x11 0 4M' basis.qcow2 >/dev/null
echo "## 1. Basis: $(gr basis.qcow2)"
qemu-img create -q -f qcow2 -F qcow2 -b basis.qcow2 s1.qcow2; qemu-io -f qcow2 -c 'write -P 0x22 0 2M' s1.qcow2 >/dev/null
qemu-img create -q -f qcow2 -F qcow2 -b s1.qcow2 s2.qcow2; qemu-io -f qcow2 -c 'write -P 0x33 2M 2M' s2.qcow2 >/dev/null
echo; echo "## 2. Kette basis <- s1 <- s2 (Größen)"; for f in basis s1 s2; do printf '  %-6s %s\n' $f "$(gr $f.qcow2)"; done
echo; echo "## 3. Kette anzeigen"; qemu-img info --backing-chain s2.qcow2 | awk '/^image:|backing file:/' | sed 's/^/  /'
echo; echo "## 4. Oberstes Abbild in die Basis zurückschreiben (commit s2 -> s1)"; qemu-img commit -q -f qcow2 s2.qcow2; printf '  s1 danach: %s\n' "$(gr s1.qcow2)"
echo; echo "## 5. Lesen aus der Kette: erste 2 MB = Muster 0x22?"; qemu-io -f qcow2 -c 'read -P 0x22 0 2M' s1.qcow2 | head -1 | sed 's/^/  /'

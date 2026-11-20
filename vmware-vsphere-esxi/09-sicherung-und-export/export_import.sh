#!/usr/bin/env bash
# Export und Wiederimport einer Platte als Modell für „VM exportieren (OVF) und wieder einspielen“ ohne die kostenpflichtige Sicherungsschnittstelle: Platte → streamOptimized-VMDK + Prüfsumme → zurück → Vergleich.
# Kein ESXi beteiligt; ein echtes OVF besteht aus einer Beschreibungsdatei, Manifest und Platten (Aufbau aus Fachwissen, nicht bestätigt).
set -eu
T=$(mktemp -d /tmp/p07-exp.XXXX); trap 'rm -rf $T' EXIT; cd $T
qemu-img create -q -f vmdk -o subformat=monolithicSparse quelle.vmdk 64M; qemu-io -f vmdk -c 'write -P 0x77 0 8M' quelle.vmdk >/dev/null
echo "## 1. Export als streamOptimized-VMDK mit Prüfsumme"; qemu-img convert -f vmdk -O vmdk -o subformat=streamOptimized quelle.vmdk export.vmdk
sha256sum export.vmdk | awk '{print "  SHA-256:", substr($1,1,16) "…"}' | tee sum.txt
echo; echo "## 2. Prüfsumme prüfen (unverändert)"; sha256sum export.vmdk | awk '{print substr($1,1,16) "…"}' | diff -q - <(sed 's/.*: //' sum.txt) >/dev/null && echo "  OK" || echo "  ABWEICHUNG"
echo; echo "## 3. Veränderte Kopie ⇒ Prüfsumme schlägt an"; cp export.vmdk bad.vmdk; printf 'X' | dd of=bad.vmdk bs=1 seek=100000 conv=notrunc 2>/dev/null; sha256sum bad.vmdk | awk '{print substr($1,1,16) "…"}' | diff -q - <(sed 's/.*: //' sum.txt) >/dev/null && echo "  OK" || echo "  ABWEICHUNG (Datei verändert)"
echo; echo "## 4. Wiederimport (zurück nach monolithicSparse) und Inhalt vergleichen"; qemu-img convert -f vmdk -O vmdk -o subformat=monolithicSparse export.vmdk zurueck.vmdk; qemu-img compare quelle.vmdk zurueck.vmdk | sed 's/^/  /'

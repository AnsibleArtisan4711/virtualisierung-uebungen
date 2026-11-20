#!/usr/bin/env bash
# Platten-Abbilder im VMDK-Format mit qemu-img: Untertypen, Größen, Umwandlung und Vergleich. Kein ESXi beteiligt; es wird nichts gestartet.
# Hinweis: Dünn/Dick (thin/thick) von VMFS-Datastores ist ein anderes Konzept (Zuteilung auf dem Datastore) und wird hier nur über Sparse-Abbilder veranschaulicht.
set -eu
T=$(mktemp -d /tmp/p07-vmdk.XXXX); trap 'rm -rf $T' EXIT; cd $T
gr() { qemu-img info "$1" | awk -F': ' '/^disk size/ {print $2; exit}'; }
echo "## 1. 64 MB virtuell, 4 MB belegte Daten, drei Untertypen"
for st in monolithicSparse monolithicFlat streamOptimized; do
  qemu-img create -q -f vmdk -o subformat=$st d-$st.vmdk 64M
  if [ $st != streamOptimized ]; then qemu-io -f vmdk -c 'write -P 0x5a 0 4M' d-$st.vmdk >/dev/null; fi
  printf '  %-18s belegt: %s\n' $st "$(gr d-$st.vmdk)"
done
echo; echo "## 2. streamOptimized aus den Daten von monolithicSparse erzeugen (Export-Format, z. B. für OVF)"
qemu-img convert -f vmdk -O vmdk -o subformat=streamOptimized d-monolithicSparse.vmdk export.vmdk; printf '  export.vmdk belegt: %s\n' "$(gr export.vmdk)"
echo; echo "## 3. Inhalt vergleichen"
qemu-img compare d-monolithicSparse.vmdk export.vmdk | sed 's/^/  /'
echo; echo "## 4. Umwandlung nach raw und zurück nach vmdk, Vergleich"
qemu-img convert -O raw d-monolithicSparse.vmdk x.raw; qemu-img convert -f raw -O vmdk x.raw y.vmdk; qemu-img compare d-monolithicSparse.vmdk y.vmdk | sed 's/^/  /'

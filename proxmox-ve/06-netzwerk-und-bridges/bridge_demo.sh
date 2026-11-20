#!/usr/bin/env bash
# Eine Linux-Bridge als virtueller Switch (das Prinzip hinter vmbr0 in Proxmox VE): zwei „Gäste“ in Netzwerk-Namespaces hängen über veth-Paare an einer Bridge und reden miteinander.
# Benötigt: ip (iproute2) mit Bridge-Unterstützung, root. VLAN-Unterstützung (8021q) ist im Testlabor nicht vorhanden und wird nicht gezeigt.
set -u
P=p06; trap 'for n in a b; do ip netns del $P-$n 2>/dev/null; done; ip link del $P-br 2>/dev/null' EXIT
echo "## 1. Bridge und zwei Gäste anlegen"
ip link add $P-br type bridge; ip link set $P-br up
for n in a b; do
  ip netns add $P-$n; ip link add v$n type veth peer name g$n
  ip link set g$n netns $P-$n; ip link set v$n master $P-br; ip link set v$n up
done
ip netns exec $P-a ip addr add 10.6.9.11/24 dev ga; ip netns exec $P-a ip link set ga up; ip netns exec $P-a ip link set lo up
ip netns exec $P-b ip addr add 10.6.9.12/24 dev gb; ip netns exec $P-b ip link set gb up; ip netns exec $P-b ip link set lo up
bridge link show 2>/dev/null | grep $P-br | sed -E 's/^[0-9]+: //; s/ state.*master/ ... master/' | sed 's/^/  /'
echo; echo "## 2. Erreichbarkeit von Gast a nach Gast b"
ip netns exec $P-a ping -c 2 -W 2 10.6.9.12 | grep -E 'transmitted'
echo; echo "## 3. Gelernte MAC-Adressen der Bridge (Weiterleitungstabelle)"
sleep 0.5; bridge fdb show br $P-br 2>/dev/null | grep -v permanent | awk '{print "  " $1, $2, $3}' | head -4
echo; echo "## 4. Gast b von der Bridge trennen: keine Verbindung mehr"
ip link set vb nomaster; ip netns exec $P-a ping -c 1 -W 1 10.6.9.12 | grep -E 'transmitted'

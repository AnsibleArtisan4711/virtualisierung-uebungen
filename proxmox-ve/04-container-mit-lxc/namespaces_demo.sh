#!/usr/bin/env bash
# Zeigt mit `unshare`, worauf Linux-Container (LXC) technisch beruhen: eigene Namensräume für Rechnername, Prozesse und Netzwerk.
# Das ist KEIN LXC und kein Proxmox; es zeigt nur das Grundprinzip. Benötigt: unshare (util-linux), ip, root.
echo "## 1. Eigener Rechnername im UTS-Namensraum"
echo "Rechnername außen: $(hostname)"
unshare -u bash -c 'hostname container01; echo "Rechnername im Namensraum: $(hostname)"'
echo "Rechnername außen danach: $(hostname)"
echo; echo "## 2. Eigener Prozess-Namensraum (PID)"
echo "Prozesse außen (Anzahl): $(ps -e --no-headers | wc -l)"
unshare -pf --mount-proc bash -c 'echo "Prozesse im Namensraum (Anzahl): $(ps -e --no-headers | wc -l)"; echo "Die Shell hat dort die PID $$"'
echo; echo "## 3. Eigener Netzwerk-Namensraum"
echo "Schnittstellen außen: $(ip -o link | wc -l)"
unshare -n bash -c 'echo "Schnittstellen im Namensraum: $(ip -o link | wc -l)"; ip -o link | cut -d: -f2'
echo; echo "## 4. Folgerung"
echo "Ein Container teilt den Kernel des Hosts; er hat eigene Sicht auf Namen, Prozesse und Netz. Eine VM hat dagegen einen eigenen Kernel."

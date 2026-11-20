#!/usr/bin/env bash
# Prüft, ob der Rechner Hardware-Virtualisierung für KVM anbietet (Voraussetzung für Proxmox VE und für verschachtelte Hypervisoren).
# Benötigt: grep, ls. Ändert nichts. Im Testlabor (Cloud-Container) ist KVM NICHT vorhanden: das Ergebnis zeigt, wie eine fehlende Unterstützung aussieht.
echo "## 1. CPU-Merkmale für Virtualisierung (vmx = Intel VT-x, svm = AMD-V)"
n=$(grep -c -E -w 'vmx|svm' /proc/cpuinfo); echo "Zeilen mit vmx/svm in /proc/cpuinfo: $n"
echo; echo "## 2. KVM-Gerät"
ls -l /dev/kvm 2>&1 | sed 's/^/  /'
echo; echo "## 3. Kernel-Module kvm, kvm_intel, kvm_amd"
if [ -r /proc/modules ]; then grep -E "^kvm" /proc/modules || echo "  (keines geladen)"; else echo "  (keine Angabe: /proc/modules ist hier nicht vorhanden)"; fi
echo; echo "## 4. Auswertung"
if [ "$n" -gt 0 ] && [ -e /dev/kvm ]; then echo "KVM nutzbar: Proxmox VE kann VMs mit Hardware-Beschleunigung starten."
else echo "KEIN KVM: Proxmox VE würde auf diesem Rechner warnen, dass Hardware-Virtualisierung fehlt; VMs liefen nur emuliert (sehr langsam) oder gar nicht."
  echo "Bei Hyper-V als Unterbau: auf dem Host bei ausgeschalteter VM 'Set-VMProcessor -VMName <Name> -ExposeVirtualizationExtensions \$true' (laut Microsoft-Dokumentation) und MAC-Adress-Spoofing für den Netzwerkadapter einschalten."
fi

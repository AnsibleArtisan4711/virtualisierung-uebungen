#!/usr/bin/env bash
# Prüft, was dieser Rechner für eine Installation von ESXi als verschachtelte VM bieten würde (CPU-Merkmale, RAM, Platz). Es wird nichts installiert.
# Richtwerte sind eigene Annahmen (NICHT aus der Herstellerdokumentation): 2 CPU-Kerne, 8 GB RAM, 40 GB Platte; ob ESXi unter Hyper-V verschachtelt läuft, ist nicht bestätigt.
set -u
echo "## 1. CPU-Merkmale (vmx/svm)"; n=$(grep -c -E 'vmx|svm' /proc/cpuinfo || true); echo "Zeilen mit vmx/svm: $n"
echo; echo "## 2. Kerne und Arbeitsspeicher"; k=$(nproc); r=$(awk '/MemTotal/ {printf "%d", $2/1048576}' /proc/meminfo); echo "Kerne: $k, RAM: ${r} GB"
echo; echo "## 3. Freier Platz in /tmp"; p=$(df -BG --output=avail /tmp | tail -1 | tr -dc 0-9); echo "Frei: ${p} GB"
echo; echo "## 4. Auswertung gegen die Richtwerte (2 Kerne, 8 GB, 40 GB, vmx/svm)"
ok=1; [ "$n" -gt 0 ] || { echo "- keine Virtualisierungserweiterung sichtbar"; ok=0; }
[ "$k" -ge 2 ] || { echo "- weniger als 2 Kerne"; ok=0; }; [ "$r" -ge 8 ] || { echo "- weniger als 8 GB RAM"; ok=0; }; [ "$p" -ge 40 ] || { echo "- weniger als 40 GB frei"; ok=0; }
[ $ok -eq 1 ] && echo "Richtwerte erfüllt (Ergebnis sagt nichts darüber, ob ESXi hier läuft)" || echo "Richtwerte NICHT erfüllt"

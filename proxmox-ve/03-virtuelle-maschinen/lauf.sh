#!/usr/bin/env bash
# Prüft beide Beispiel-Konfigurationen.
cd "$(dirname "$0")"; for k in 100.conf 101.conf; do python3 vm_conf_pruefen.py $k; done

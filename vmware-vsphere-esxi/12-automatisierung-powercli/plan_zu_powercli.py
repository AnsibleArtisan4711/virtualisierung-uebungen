#!/usr/bin/env python3
"""Erzeugt aus einem Plan (JSON) PowerCLI-Befehle als TEXT. Es wird NICHTS ausgeführt (kein PowerShell, kein ESXi vorhanden). Befehlsform aus Fachwissen, NICHT gegen die Dokumentation geprüft – vor Verwendung prüfen!
Der kostenlose ESXi lässt laut KB 399823 (gelesen 20.11.2026) nur eine eingeschränkte/lesende API zu; schreibende Automatisierung ist dort möglicherweise nicht möglich (nicht geprüft)."""
import json
PLAN = json.loads('[{"name": "web01", "ds": "datastore1", "gb": 20, "mem": 2048, "cpu": 2, "pg": "VM Network"}, {"name": "db01", "ds": "datastore1", "gb": 40, "mem": 4096, "cpu": 2, "pg": "Intern"}]')
def befehle(v): return ['New-VM -Name %(name)s -Datastore %(ds)s -DiskGB %(gb)d -MemoryMB %(mem)d -NumCpu %(cpu)d -NetworkName "%(pg)s"' % v, 'Start-VM -VM %(name)s' % v]
if __name__ == '__main__':
    print('Connect-VIServer -Server <esxi-adresse>   # Anmeldeinformationen NICHT im Skript ablegen\n')
    for v in PLAN: print('# ' + v['name']); print('\n'.join(befehle(v))); print()
    print('Summe: %d VMs, %d MB RAM, %d GB Platte (Plan, nicht ausgeführt)' % (len(PLAN), sum(v['mem'] for v in PLAN), sum(v['gb'] for v in PLAN)))

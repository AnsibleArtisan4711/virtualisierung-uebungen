#!/usr/bin/env python3
"""Prüft eine geplante Laborumgebung gegen die Grenzen des kostenlosen ESXi, wie sie in Broadcom-KB 399823 „VMware ESXi 8.0 Update 3e now available as a Free Hypervisor“ gelesen wurden (Abruf 20.11.2026):
höchstens 2 physische CPUs je Host, höchstens 8 vCPUs je VM, kein vCenter, kein vMotion/DRS/HA, keine Sicherung über die VADP-Schnittstelle, nur Host Client, API nur lesend bzw. eingeschränkt, kein offizieller Support.
Die Seite nennt kein Datum; Angaben können sich ändern – vor Einsatz erneut prüfen. Die Beispiel-Pläne sind erfunden."""
GRENZEN = {'cpu_sockel': 2, 'vcpu_je_vm': 8}
NICHT = {'vcenter': 'kein vCenter', 'vmotion': 'kein vMotion', 'drs': 'kein DRS', 'ha': 'kein HA', 'vadp_backup': 'keine Sicherung über VADP', 'schreibende_api': 'API nur lesend/eingeschränkt'}
def pruefe(plan):
    m = []
    if plan['cpu_sockel'] > GRENZEN['cpu_sockel']: m.append('%d Sockel geplant, erlaubt %d' % (plan['cpu_sockel'], GRENZEN['cpu_sockel']))
    for vm, v in plan['vms'].items():
        if v > GRENZEN['vcpu_je_vm']: m.append('VM %s mit %d vCPUs, erlaubt %d' % (vm, v, GRENZEN['vcpu_je_vm']))
    for f in plan['funktionen']:
        if f in NICHT: m.append('Funktion nicht verfügbar: ' + NICHT[f])
    return m
PLAENE = {'Labor klein': {'cpu_sockel': 1, 'vms': {'dc01': 2, 'web01': 4}, 'funktionen': []},
          'Cluster-Wunsch': {'cpu_sockel': 2, 'vms': {'db01': 12, 'web01': 2}, 'funktionen': ['vcenter', 'vmotion', 'ha']},
          'Backup-Wunsch': {'cpu_sockel': 1, 'vms': {'file01': 4}, 'funktionen': ['vadp_backup']}}
if __name__ == '__main__':
    for n, p in PLAENE.items():
        m = pruefe(p); print('%-15s %s' % (n, 'passt' if not m else 'PASST NICHT')); [print('   -', x) for x in m]

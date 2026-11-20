#!/usr/bin/env python3
"""Modell für Zulassungsprüfung (Admission Control) und einfache Lastverteilung in einem Cluster (erfundene Werte; Verfahren stark vereinfacht, aus Fachwissen, nicht gegen Herstellerdokumentation geprüft).
Frage 1: Passen alle VMs noch auf die verbleibenden Hosts, wenn der größte Host ausfällt? Frage 2: Welche VM würde man zur Entlastung verschieben (einfaches Greedy-Verfahren)?
Gilt nur mit vCenter und passender Lizenz; der kostenlose ESXi hat weder HA noch DRS (KB 399823, gelesen 20.11.2026)."""
HOSTS = {'esx1': 64, 'esx2': 64, 'esx3': 32}                      # GB RAM
VMS = {'db01': ('esx1', 32), 'web01': ('esx1', 16), 'app01': ('esx2', 24), 'dc01': ('esx2', 8), 'test01': ('esx3', 12)}
def last(hosts, vms): return {h: sum(g for n, (hh, g) in vms.items() if hh == h) for h in hosts}
def ausfall(host):
    rest = {h: c for h, c in HOSTS.items() if h != host}; frei = {h: rest[h] - l for h, l in last(rest, {n: v for n, v in VMS.items() if v[0] != host}).items()}
    nicht = []
    for n, (h, g) in sorted(VMS.items(), key=lambda x: -x[1][1]):
        if h != host: continue
        z = max(frei, key=frei.get)
        if frei[z] >= g: frei[z] -= g
        else: nicht.append(n)
    return nicht
if __name__ == '__main__':
    l = last(HOSTS, VMS); print('Last je Host:', ', '.join('%s %d/%d GB (%.0f %%)' % (h, l[h], HOSTS[h], 100 * l[h] / HOSTS[h]) for h in HOSTS))
    print('\nAusfalltest:')
    for h in HOSTS: n = ausfall(h); print('  Ausfall %s: %s' % (h, 'alle VMs finden Platz' if not n else 'KEIN Platz für ' + ', '.join(n)))
    voll = max(HOSTS, key=lambda h: l[h] / HOSTS[h]); leer = min(HOSTS, key=lambda h: l[h] / HOSTS[h]); print('\nLastverteilung: %s ist am vollsten (%.0f %%), %s am leersten (%.0f %%)' % (voll, 100 * l[voll] / HOSTS[voll], leer, 100 * l[leer] / HOSTS[leer]))

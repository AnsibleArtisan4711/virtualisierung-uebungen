#!/usr/bin/env python3
"""Liest eine .vmx-Datei (Zeilen `schlüssel = "wert"`; erfundenes Beispiel, Schlüssel aus Fachwissen, NICHT gegen Herstellerdokumentation geprüft) und prüft einfache Regeln:
Pflichtschlüssel, vCPU-Zahl, Arbeitsspeicher, vmxnet3/pvscsi, Netzwerkname, Plattendatei vorhanden."""
import sys, re
def lies(pfad):
    d = {}
    for z in open(pfad, encoding='utf-8'):
        m = re.match(r'\s*([\w.:]+)\s*=\s*"(.*)"\s*$', z)
        if m: d[m.group(1)] = m.group(2)
    return d
def pruefe(c):
    m = []
    for k in ('displayName', 'guestOS', 'memSize', 'numvcpus'):
        if k not in c: m.append('Pflichtschlüssel fehlt: ' + k)
    if int(c.get('memSize', 0)) < 512: m.append('Arbeitsspeicher unter 512 MB')
    if int(c.get('numvcpus', 1)) > 8: m.append('mehr als 8 vCPUs (Grenze des kostenlosen ESXi)')
    if c.get('ethernet0.virtualDev', 'e1000') != 'vmxnet3': m.append('Netzwerkkarte nicht vmxnet3')
    if c.get('scsi0.virtualDev', 'lsilogic') != 'pvscsi': m.append('SCSI-Controller nicht pvscsi')
    if not c.get('ethernet0.networkName'): m.append('keine Portgruppe (networkName)')
    if not c.get('scsi0:0.fileName', '').endswith('.vmdk'): m.append('Platte scsi0:0 ohne .vmdk')
    return m
if __name__ == '__main__':
    for f in (sys.argv[1:] or ['web01.vmx']):
        c = lies(f); print('%s: %s MB, %s vCPU' % (c.get('displayName', '?'), c.get('memSize', '?'), c.get('numvcpus', '?')))
        m = pruefe(c); print('\n'.join('  Hinweis: ' + x for x in m) or '  alle Regeln erfüllt')

#!/usr/bin/env python3
"""Erzeugt aus einer kleinen Beschreibung (JSON) die zugehörigen qm-Befehle als TEXT. Es wird NICHTS ausgeführt (keine Proxmox-Umgebung vorhanden).
Die Befehlsform folgt dem Muster `qm create <vmid> --name … --memory … --cores … --net0 virtio,bridge=…` (Befehlsform aus Fachwissen, nicht bestätigt – gegen die Handbuchseite qm(1) prüfen!)."""
import json
PLAN = json.loads("""[
 {"vmid": 200, "name": "web01", "memory": 2048, "cores": 2, "bridge": "vmbr0", "disk_gb": 16, "storage": "local-lvm"},
 {"vmid": 201, "name": "db01",  "memory": 4096, "cores": 2, "bridge": "vmbr1", "disk_gb": 32, "storage": "local-lvm"}
]""")
def befehle(v):
    return ['qm create %(vmid)d --name %(name)s --memory %(memory)d --cores %(cores)d --net0 virtio,bridge=%(bridge)s' % v,
            'qm set %(vmid)d --scsi0 %(storage)s:%(disk_gb)d' % v, 'qm start %(vmid)d' % v]
if __name__ == '__main__':
    for v in PLAN:
        print('# VM %(vmid)d (%(name)s)' % v); print('\n'.join(befehle(v))); print()
    print('Summe: %d VMs, %d MiB RAM, %d GB Platte (Plan, nicht ausgeführt)' % (len(PLAN), sum(v['memory'] for v in PLAN), sum(v['disk_gb'] for v in PLAN)))

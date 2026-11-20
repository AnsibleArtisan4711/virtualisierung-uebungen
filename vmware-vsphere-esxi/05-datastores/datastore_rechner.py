#!/usr/bin/env python3
"""Rechnet Kapazität eines Datastores mit dünn (thin) und dick (thick) zugeteilten virtuellen Platten (erfundene Werte; Rechnung einfach, Begriffe aus Fachwissen).
Zeigt Überbuchung und warnt, wenn die tatsächliche Belegung eine Schwelle (80 %) übersteigt."""
DATASTORE_GB = 500
DISKS = [('dc01', 60, 'thick', 60), ('web01', 100, 'thin', 22), ('db01', 200, 'thin', 130), ('file01', 400, 'thin', 150), ('test01', 80, 'thin', 8)]  # (VM, zugeteilt, Art, belegt)
def rechne(ds, disks):
    z = sum(d[1] for d in disks); b = sum(d[3] if d[2] == 'thin' else d[1] for d in disks)
    return z, b
if __name__ == '__main__':
    z, b = rechne(DATASTORE_GB, DISKS)
    print('%-8s %9s %6s %8s' % ('VM', 'zugeteilt', 'Art', 'belegt'))
    for n, g, a, u in DISKS: print('%-8s %6d GB %6s %5d GB' % (n, g, a, u if a == 'thin' else g))
    print('\nDatastore: %d GB' % DATASTORE_GB); print('Zugeteilt:  %d GB (%.0f %% des Datastores, Überbuchung)' % (z, 100 * z / DATASTORE_GB)); print('Belegt:     %d GB (%.0f %%)' % (b, 100 * b / DATASTORE_GB))
    if b / DATASTORE_GB > 0.8: print('WARNUNG: Belegung über 80 %')
    wachs = 150; print('Wachstum bei +%d GB in db01: Belegung %.0f %% %s' % (wachs, 100 * (b + wachs) / DATASTORE_GB, '-> Datastore VOLL, thin-VMs bleiben stehen' if b + wachs > DATASTORE_GB else ''))

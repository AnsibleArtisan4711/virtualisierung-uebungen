#!/usr/bin/env python3
"""Rechnet das Mehrheitsprinzip (Quorum) eines Clusters nach: Jeder Knoten hat eine Stimme, Mehrheit = mehr als die Hälfte der Stimmen. Optional ein externer Entscheider (QDevice).
Regeln nach der gelesenen Proxmox-Dokumentation (Cluster Manager): ohne Quorum ist das Cluster-Dateisystem schreibgeschützt; bei geraden Knotenzahlen kann ein QDevice eine Stimme beisteuern;
bei ungeraden Knotenzahlen wird davon abgeraten. Die Berechnung selbst ist einfache Mathematik."""
def mehrheit(stimmen): return stimmen // 2 + 1
def pruefe(knoten, ausgefallen, qdevice=False, qd_erreichbar=True):
    gesamt = knoten + (1 if qdevice and knoten % 2 == 0 else 0)
    da = knoten - ausgefallen + (1 if qdevice and knoten % 2 == 0 and qd_erreichbar else 0)
    return gesamt, da, da >= mehrheit(gesamt)
if __name__ == '__main__':
    print('%-8s %-9s %-8s %-18s %-8s %-8s %s' % ('Knoten', 'QDevice', 'Ausfall', 'Stimmen (da/gesamt)', 'Mehrheit', 'Quorum', 'Folge'))
    for k, q, a, qe in [(3, False, 0, True), (3, False, 1, True), (3, False, 2, True), (2, False, 1, True), (2, True, 1, True), (2, True, 1, False), (4, False, 2, True), (4, True, 2, True), (5, False, 2, True), (5, False, 3, True)]:
        g, d, ok = pruefe(k, a, q, qe)
        folge = 'normal' if ok else 'Cluster-Dateisystem nur lesbar, HA hält an'
        print('%-8d %-9s %-8d %-18s %-8d %-8s %s' % (k, ('ja' if q else 'nein') + ('' if qe or not q else ' (aus)'), a, '%d/%d' % (d, g), mehrheit(g), 'ja' if ok else 'NEIN', folge))

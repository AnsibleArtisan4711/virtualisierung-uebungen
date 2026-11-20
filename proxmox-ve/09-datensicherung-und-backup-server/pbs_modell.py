#!/usr/bin/env python3
"""Einfaches Modell der Arbeitsweise eines Backup-Servers mit Chunk-Deduplizierung (Vorbild: Proxmox Backup Server; vereinfacht und erfunden, KEIN Code von Proxmox):
Daten werden in Blöcke fester Größe geteilt, jeder Block per SHA-256 adressiert; gleiche Blöcke werden nur einmal gespeichert.
Aufräumen (Prune) entfernt nur Sicherungs-Einträge, der Platz wird erst durch die Speicherbereinigung (GC) frei – so beschreibt es die gelesene PBS-Dokumentation."""
import hashlib, os, random
BLOCK = 4096
class Speicher:
    def __init__(s): s.chunks = {}; s.snaps = {}
    def sichern(s, name, daten):
        ids = []
        for i in range(0, len(daten), BLOCK):
            b = daten[i:i + BLOCK]; h = hashlib.sha256(b).hexdigest()
            s.chunks.setdefault(h, len(b)); ids.append(h)
        s.snaps[name] = ids
    def prune(s, behalten): 
        for n in [n for n in s.snaps if n not in behalten]: del s.snaps[n]
    def gc(s):
        benutzt = {h for ids in s.snaps.values() for h in ids}
        weg = [h for h in s.chunks if h not in benutzt]
        for h in weg: del s.chunks[h]
        return len(weg)
    def belegt(s): return sum(s.chunks.values())
def zeige(s, text): print('%-48s Chunks: %4d  belegt: %7d Bytes  Sicherungen: %s' % (text, len(s.chunks), s.belegt(), ', '.join(s.snaps) or '-'))
if __name__ == '__main__':
    random.seed(6); disk = bytearray(random.randbytes(BLOCK * 200))       # 200 Blöcke, 800 KiB
    s = Speicher(); s.sichern('tag1', bytes(disk)); zeige(s, '1. Erste Sicherung (200 Blöcke)')
    s.sichern('tag2', bytes(disk)); zeige(s, '2. Zweite Sicherung, nichts geändert')
    for b in (3, 77, 150): disk[b * BLOCK:(b + 1) * BLOCK] = random.randbytes(BLOCK)
    s.sichern('tag3', bytes(disk)); zeige(s, '3. Dritte Sicherung, 3 Blöcke geändert')
    s.prune({'tag3'}); zeige(s, '4. Prune: tag1 und tag2 entfernt (Chunks bleiben)')
    n = s.gc(); zeige(s, '5. Speicherbereinigung (GC): %d Chunks frei' % n)
    print('\nOhne Deduplizierung wären drei Sicherungen je %d Bytes = %d Bytes belegt; hier: %d Bytes nach Schritt 3.' % (BLOCK * 200, 3 * BLOCK * 200, 203 * BLOCK))

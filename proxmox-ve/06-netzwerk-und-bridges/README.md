# 06 Netzwerk

Übung **06.1** (Priorität 1). Geschätzte Zeit: 5 bis 7 Stunden (Schätzung; Lehrplan: 9 UE zu 45 Minuten = 6,75 Stunden).

> Skripte im Container ausgeführt; VLAN nicht geprüft.

| Datei | Zweck |
|---|---|
| `06.1-netzwerk-und-bridges.md` | Die Übung mit Aufgaben, Kontrollfragen und Musterlösung |
| `bridge_demo.sh` | Eine Linux-Bridge als virtueller Switch (das Prinzip hinter vmbr0 in Proxmox VE): zwei „Gäste“ in Netzwerk-Namespaces hängen über veth-Paare an einer Bridge und reden miteinander. |
| `interfaces` | Skript |
| `interfaces_pruefen.py` | Prüft eine Netzwerkkonfiguration im Format von /etc/network/interfaces (Beispiel angelehnt an die Proxmox-Dokumentation, aber erfunden) auf einfache Fehler: |
| `lauf.sh` | Startet interfaces_pruefen.py und schreibt die Ausgabe. |
| `beispiele/bridge_demo.ausgabe.txt` | Echte Ausgabe des Laufs von `bridge_demo` |
| `beispiele/lauf.ausgabe.txt` | Echte Ausgabe des Laufs von `lauf` |

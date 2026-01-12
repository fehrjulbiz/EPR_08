# Code Review 3 - Ökosystem

### Grundaufbau:

Ökosystem:

- Space
- entities (carnivores, herbivores, omnivores, Plants)
- Jahrezeiten

Übergruppen:

- Pflanze
- Tier

Pflanzen:

- summer_plant ( wächst 2x so schnell im sommer, garnicht im winter)
- winter_plant ( wächst 1,5x im winter, 1x im sommer)
- poison_plant ( wenn allesfresser sie essen haben sie eine 15% warscheinlihkeit zu sterben. Wenn sie es tun dann verliert die Pflanze keine Fläche)

Tiere:

- Fleischfresser: 
- ernähren sich von Planzen - / Allesfressern
- machen Winterschlaf wenn genug Energie übrig ist
- wenn viel Beute da ist und die Jadg gut verläuft vermehren sie sich relativ schnell
- Allesfresser: 
- ernähren sich von Pflanzen / Fleischfressern und Pflanzenfressern

zentraler aufbau der Lebewesen:
- energie 
- größe 
- max space 
- min space

Wachstum,  chance auf vermehrung ab gewissem Energielevel und ab gewissem alter. 

- Winterschlaf wenn energie reicht, sonst tod

### Rundenkonzept:

- rede runde wird eine interact function aufgerufen, die abhängig ist von Jahreszeit
- bei der interact function geht es generell darum, sich zu ernähren, zu wachsen und sich zu vermehren. Im generellen mit seiner Umgebung zu interagieren.
- Das kann unterschiedlich aussehen bei den verschiedenen Arten von Lebewesen.
- Wenn es winter ist. gibt es verschiedene factoren die angepasst werden. z.b dass der jagderfolg runtergesetzt wird. oder das bestimmte pflanzen schneller oder langsamer wachsen
- Zudem gibt es wenn es winter ist eine sleep funktion für tiere die nur aufgerufen wird wenn die energie mindestens 3 ist ansonsten stirbt das Tier mit del
- wenn bestimmte energielevel erreicht sind, dann vermehren sich tiere und sie wachsen bis sie ein maximal größe erreicht haben. Bei pflanzen ist es genau so

UI:
- user gibt Runden an und für jede zweite runde wird dann change season aufgerufen. 
- jede runde wird interact aufgerufen mit den spezifischen Werten für dinge wie jadgerfolg für Tiere oder wachstumsrate für Pflanzen.
- jede Runde wird am ende das ergebnis geprintet also spacetaken, space left, entities in einem Sinnvollen format, oder am ende wenn alle runden aufgebraucht sind und alle daten werden einfach zwischengespeichert. 
- die jagd ist von random,randint bestimmt und wird mit einem bool wert wie hunt > 0.50 zb und die jagderfolgchancen werden dann somit variiert dass start und limit von random.randint variable verändert werden. will man die chance erhöhen wird zb der start veringert und wenn es bsp winter ist, wird das limit veringert. Dadurch ist der random wert trzdm variable änderbar.
- wird bei der eat function von tieren eine pflanze gegessen, so wird ihre größe veringert, wenn ein tier gegessen wird, so wird das energielevel auf 0 gesenkt. am ende jeder runde wird ein checkup gemacht ob die tiere genug energie haben (normalerweise energie > 0 dann leben, im winter energie > 3 dann winterschlaf, sonst tot. Bei pflanzen ist der Checkup, dass die pflanze eine gewisse Größe hat, ist sie nicht groß genug, stirbt sie. 

### Habitat:

- Zentrale Daten: space, season, entity-collections
- Speicherung und zentraler Ort des ecosystems
- Rundenlogik findet hier zentral statt wie auch der Wechsel der jahreszeiten

**Regeln:**

- Alle 2 Runden wechselt die Jahreszeit
- Das Habitat startet im Frühling

---

### Lebewesen:

- enthalten: id, species ( name = species + id) , age
- hier wird das Lebewesen erst initialisiert
- Daten werden an spezifische spezies Klasse weitergegeben

**Regeln**

---

### Pflanzen:

- enthalten, id, species, name, energy/size, growth_rate ( wie viel size pro runde wächst), min_size, max_size
- Kernfunktionen sind wachsen, vermehren
- jede runde wachsen sie basierend auf einem wachstumsfaktor

**Regeln:** 

- wenn am ende einer Runde, size < min_size —> dann stirbt die Pflanze und ihre instanz wird gelöscht          ?(Tod möglicherweise dokumentiert)
- Pflanzen können sich nur ab size ≥ 5 vermehren
- sie werden initialisiert mit größe = 1
- wenn ein tier sie isst, verliert sie an size
- jede runde wachsen sie um wachstumsfaktor: standard = 1
- gibt es in dem habitat kein platz mehr, so wächst die Pflanze nichtmehr weiter

### Tiere:

- enthalten auch wie Pflanzen
Dokumentation
EPR UE08
Fehr, 8766674
Schidlauskat, 7791598

1.	Ziel des Projekts
Im Rahmen des Moduls EPR wurde eine Simulation eines Ökosystems in Python entwickelt. 
Ziel war es verschiedene Lebewesen (Pflanzen und Tiere) sowie ihre Aktionen in einem begrenzten Lebensraum nachvollziehbar zu modellieren. 
Die Simulation sollte die Interaktion der einzelnen Objekte über mehrere Runden hinweg abbilden. Lebewesen konnten in diesem Ökosystem wachsen, essen, sich fortpflanzen, Energie verbrauchen und sterben. 
Das Projekt wurde mithilfe objektorientierter Programmierung umgesetzt.

2.	Grundidee des Ökosystems
Das Ökosystem wurde als geschlossenes Habitat betrachtet, in dem alle Lebewesen um Platz und Nahrung konkurrieren. 
Die Simulation verläuft rundenweise, wobei jede Runde eine Zeiteinheit darstellt. 
Die Lebewesen verhalten sich innerhalb der diskreten Runden abhängig von ihrem Typ und der aktuellen Jahreszeit. 
Hierbei haben Pflanzen und Tiere verschiedene Eigenschaften. Pflanzen können wachsen oder sterben. Tiere können fressen, dadurch Energie gewinnen, Energie verlieren, sich fortpflanzen oder auch sterben.

3.	Aufbau
Das Programm besteht aus mehreren Klassen.
Habitat: Über das Habitat wird alles gesteuert. Es verwaltet alle Pflanzen und Tiere, den verfügbaren Platz, die Jahreszeiten und den Ablauf der Simulation. Es entfernt tote Lebewesen und loggt alle Ereignisse.
LivingBeing (abstrakt): Dies ist die Basisklasse für alle Lebewesen. Über sie sind gemeinsame Eigenschaften wie Alter, Zustand (lebendig, schlafend, tot) und eine eindeutige ID definiert.
Plant (abstrakt): Dies ist die Oberklasse aller Pflanzen. Pflanzen haben eine Größe, die sowohl für ihren Platzverbrauch als auch ihre „Körpergröße“ steht.
Animal (abstrakt): Dies ist die Oberklasse aller Tiere. Tiere besitzen Energie, die sie auch pro Runde zu einem Stück verbrauchen und müssen Nahrung finden, um wieder Energie zu gewinnen und somit zu überleben.
Die verschiedenen Pflanzen- und Tierarten sind als Unterklassen umgesetzt worden.

4.	Regeln des Ökosystems
Allgemein:
•	Die Simulation läuft in diskreten Runden
•	Alle Lebewesen altern um eine Einheit pro Runde
•	Lebewesen markieren sich als tot, löschen sich aber nicht selbst
•	Tote Lebewesen werden demnach am Ende einer Runde durch das Habitat entfernt
Regeln für Pflanzen:
•	Pflanzen besitzen eine minimale und maximale Größe
•	Ihr Wachstum hängt von ihrer Art und der Jahreszeit ab
•	Wenn eine Pflanze gefressen wird, reduziert sich ihre Größe
•	Wenn ihre Größe dadurch unter die minimale Größe fällt, stirbt sie
•	Pflanzen können sich mit einer 50% Wahrscheinlichkeit fortpflanzen, sofern sie alt genug und groß genug sind
•	Pflanzenarten sind: 
o	SummerPlant: Wachstum im Sommer am stärksten
o	WinterPlant: Wachstum im Winter am stärksten
o	Poison Plant: Wachstum konstant, kann Omnivores beim Fressen vergiften
Regeln für Tiere
•	Tiere verlieren eine Energieeinheit pro Runde, es sei denn sie halten Winterschlaf, dort haben sie keinen Energieverlust
•	Tiere müssen fressen, um Energie zu gewinnen
•	Tiere können sich mit 50 prozentiger Wahrscheinlichkeit fortpflanzen, sofern sie alt genug sind und genug Energie haben
•	Tiere sterben bei einem Energie Level von oder unter Null
•	Tierarten sind: 
o	Herbivore: Frisst Pflanzen
o	Carnivore: Frisst / Jagt Tiere
o	Omnivore: Frisst / Jagt Pflanzen und Tiere
Spezialregeln:
•	Wenn ein Omnivore eine PoisonPlant isst, verliert es mit einer Wahrscheinlichkeit von 30% Energie
•	Alle Tiere (Herbivore, Carnivore, Omnivore) halten im Winter Winterschlaf, wenn sie genügend Energie haben, andererseits sterben sie. Sobald sich die Jahreszeit ändert, wachen sie aus dem Winterschlaf auf.
•	Pflanzen können sich nur reproduzieren und wachsen, wenn genug Platz im Habitat verfügbar ist
•	Tiere können sich nur reproduzieren, wenn genug Platz im Habitat verfügbar ist
•	Der Jagderfolg von Carnivoren ist im Herbst 30%, sonst 60%

5.	Rundenablauf
Jede Runde folgt einer festen Reihenfolge:
1.	Initialisierung (Event-Log leeren)
2.	Pflanzenphase (Wachstum, Reproduktion, Tod)
3.	Tierphase (Energieverbrauch, Fressen, Reproduktion, Winterschlaf oder Tod)
4.	Cleanup-Phase (Entfernen toter Lebewesen)
5.	Logging und Ausgabe der Ergebnisse

6.	Zufälle in der Simulation
Mehrere Aspekte des Systems sind zufallsbasiert:
•	Jagderfolg von Tieren
•	Fortpflanzung von Pflanzen und Tieren
•	Vergiftung durch PoisonPlants

7.	Logging von Ereginissen
Jede Aktion erzeugt ein Ereginis, z.B.:
•	Wachstum einer Pflanze
•	Fressen einer Pflanze oder eines Tieres
•	Tod eines Lebewesens
•	Wechsel der Jahreszeit
Am Ende jeder Runde wird eine Übersicht über alle Ereignisse und den aktuellen Stand (Anzahl Pflanzen/Tiere) ausgegeben.

8.	Benutzerhandbuch (UI)
Nach dem Start des Programms wird der Benutzer über die Konsole nach einer Startkonfiguration gefragt (Größe des Habitats, Anzahl der Lebewesen).
Die main.py Datei enthält das Nutzerprogramm zur Eingabe der Startwerte und die Intialisierung der Simulation. Dazu werden die Klassen aus ecosystem.py und die run_simulation Funktion aus round.py zur Ausführung der Simulation genutzt. Der Nutzer wird nach dem Platz im Habitat, der Anzahl der Runden der Simulation und der Anzahl der jeweiligen Lebewesen in dem Habitat gefragt. Bei jeder nutzereingabe prüft die ask_number Funktion ob die Eingabe eine valide int >= 0 ist. Nach der Fertigstellung der Nutzereingaben startet das Programm die Simulation und gibt dabei alle Rundeninformationen und Endinformationen nach Ablauf der angegebenen Runden aus.

9.	Annahmen
•	Alterstod wird indirekt über den Energieverlust modelliert
•	Alle Lebewesen altern gleichmäßig pro Runde
•	Jahreszeiten wechseln alle zwei Runden in fester Reihenfolge

10.	 Konkrete Werte zu den Regeln
Pflanzen
•	Startgröße: 3
•	min_size: 3
•	max_size: 10
•	Reproduktion möglich ab: age > 2 und size ≥ 4
•	Reproduktionswahrscheinlichkeit: 50%
•	SummerPlant Wachstum: +2 (summer), +1 (spring/autumn), +0 (winter)
•	WinterPlant Wachstum: +2 (winter), sonst +1
•	PoisonPlant Wachstum: +1 immer
•	Beim Fressen: Plant verliert pro Bite 1 (weil get_eaten(1))

Tiere
•	Startenergie: 5
•	Energieverlust pro Runde: -1 (außer sleeping)
•	Reproduktion möglich ab: age > 2 und energy ≥ 6
•	Reproduktionswahrscheinlichkeit: 50%
•	Herbivore: wenn Essen klappt: +2 Energie
•	Carnivore/Omnivore wenn Tier gegessen: +3 Energie
•	Herbivore findet Essen nur mit 70% Chance (weil fail wenn random() >= 0.7)
•	Omnivore “findet” Essen nur mit 60% Chance
•	Carnivore Jagderfolg: 30% im Herbst, sonst 60%
•	Winterschlaf-Regel (wie implementiert): im Winter, wenn energy ≥ 3: sleeping, sonst Tod
•	PoisonPlant Effekt: 30% Chance, dann -3 Energie (und ggf. Tod)






   

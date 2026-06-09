UE08

author = "8766674, Fehr, 7791598, Schidlauskat"

Dieses Projekt implementiert ein simulationsbasiertes Ökosystem mithilfe objektorientierter Programmierung in Python. Das Ökosystem besteht aus einem Habitat, Pflanzen und Tieren, die in diskreten Runden interagieren.

##Ziel und Anforderungen

Ziel des Projekts ist die Umsetzung der Aufgabenstellung „Ökosystem – der Lauf der Natur“ aus EPR WiSe 2025/26.

Umgesetzt wurden:

Simulation in diskreten Runden
mindestens 3 Pflanzenarten
mindestens 3 Tierarten (Herbivore, Carnivore, Omnivore)
begrenzter Platz im Habitat
Wachstum, Fressen, Reproduktion, Tod
zufallsbasierte Ereignisse
Konsolenbasiertes UI
##Programmstruktur

Zentrale Klassen:

ConsoleUI Steuert Benutzereingaben und den Ablauf der Simulation

Habitat Zentraler Orchestrator des Systems. Verwaltet alle Lebewesen, den verfügbaren Platz, die Jahreszeiten und den Rundenablauf

LivingBeing (abstrakt) Basisklasse für alle Lebewesen

Plant (abstrakt) Oberklasse aller Pflanzenarten. Spezialisierungen: SummerPlant, WinterPlant, PoisonPlant

Animal (abstrakt) Oberklasse aller Tiere. Spezialisierungen: Herbivore, Carnivore, Omnivore

##Regeln des Ökosystems

Allgemeine Regeln:

Die Simulation läuft in diskreten Runden
In jeder Runde altern alle Lebewesen
Tote Lebewesen werden am Ende der Runde entfernt
Pflanzen:

Pflanzen besitzen eine minimale und maximale Größe
Das Wachstum ist abhängig von Pflanzenart und Jahreszeit
Wird die minimale Größe unterschritten, stirbt die Pflanze
Tiere:

Tiere verlieren pro Runde Energie
Tiere müssen fressen, um zu überleben
Reproduktion ist alters- und energieabhängig
Fleischfresser und Allesfresser können jagen
##Spezialregeln

Wenn ein Tier eine PoisonPlant isst, verliert das Tier mit einer Wahrscheinlichkeit von 30% Energie, statt welche zu gewinnen

Carnivoren halten im Winter Winterschlaf, sofern ihre Energie ≥ 3 ist

Pflanzen können nur wachsen, wenn im Habitat noch freier Platz vorhanden ist

Der Jagderfolg von Carnivoren ist jahreszeitenabhängig

Tiere sterben sofort, wenn ihre Energie ≤ 0 fällt

##Zufallseinflüsse

Jagderfolg von Tieren

Vergiftung durch PoisonPlant

Reproduktion von Pflanzen und Tieren

##UI

Nach dem Start wird der Benutzer über die Konsole nach der Startkonfiguration gefragt (Habitatgröße, Anzahl der Lebewesen)

Nach der Initialisierung kann:

eine einzelne Runde simuliert werden
mehrere Runden simuliert werden
die Simulation pausiert werden
Die Ausgabe zeigt nach jeder Runde den aktuellen Zustand des Ökosystems (season, Anzahl Tier, Anzahl Pflanzen, Ereignisse)

Voraussetzungen:

Python 3.10+
##Annahmen

Tod durch Altersschwäche wird indirekt über den Energieverlust modelliert
Alle Lebewesen altern pro Runde um 1
Jahreszeiten wechseln alle zwei Runden (Start bei Frühling, dann Sommer, Herbst, Winter)

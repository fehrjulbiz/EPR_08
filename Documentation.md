# 🌿 Ökosystem-Simulation (EPR UE08)

Dieses Repository enthält die Dokumentation und Implementierung einer rundenbasierten Ökosystem-Simulation in Python, die im Rahmen des Moduls **Einführung in die Programmierung (EPR)** entwickelt wurde.

---

## 📋 Projekt-Metadaten

* **Modul:** Einführung in die Programmierung (EPR) – Übung 08
* **Entwickler:**
    * **Fehr** (Matrikelnummer: 8766674)
    * **Schidlauskat** (Matrikelnummer: 7791598)
* **Programmiersprache:** Python 3 (Objektorientierter Ansatz)

---

## 1. Ziel des Projekts

Im Rahmen des Moduls EPR wurde eine Simulation eines Ökosystems in Python entwickelt. Ziel war es, verschiedene Lebewesen (Pflanzen und Tiere) sowie ihre Aktionen in einem begrenzten Lebensraum nachvollziehbar zu modellieren.

Die Simulation bildet die Interaktion der einzelnen Objekte über mehrere Runden hinweg ab. Lebewesen können in diesem Ökosystem wachsen, fressen, sich fortpflanzen, Energie verbrauchen und sterben. Das Projekt wurde vollständig mithilfe von **objektorientierter Programmierung (OOP)** umgesetzt.

---

## 2. Grundidee des Ökosystems

Das Ökosystem wird als geschlossenes Habitat betrachtet, in dem alle Lebewesen um Platz und Nahrung konkurrieren. 

* **Rundenbasiert:** Die Simulation verläuft rundenweise, wobei jede Runde eine diskrete Zeiteinheit darstellt.
* **Dynamisch:** Die Lebewesen verhalten sich innerhalb der Runden abhängig von ihrem Typ und der aktuellen Jahreszeit.
* **Eigenschaften:**
    * **Pflanzen** können wachsen oder sterben.
    * **Tiere** können fressen, dadurch Energie gewinnen, Energie verlieren, sich fortpflanzen oder sterben.

---

## 3. Architektur & Klassenaufbau

Das Programm ist modular aufgebaut und teilt sich in verschiedene, logische Klassen auf:

* **`Habitat`**: Die zentrale Steuerungseinheit. Es verwaltet alle Pflanzen und Tiere, den verfügbaren Platz, die Jahreszeiten sowie den gesamten Ablauf der Simulation. Zudem entfernt es tote Lebewesen und loggt alle Ereignisse.
* **`LivingBeing` (abstrakt)**: Die Basisklasse für alle Lebewesen. Sie definiert gemeinsame Eigenschaften wie das Alter, den Zustand (lebendig, schlafend, tot) und eine eindeutige ID.
* **`Plant` (abstrakt)**: Die Oberklasse aller Pflanzen. Pflanzen besitzen eine Größe, die sowohl für ihren Platzverbrauch als auch ihre „Körpergröße“ steht.
* **`Animal` (abstrakt)**: Die Oberklasse aller Tiere. Tiere besitzen Energie, die sie pro Runde verbrauchen. Sie müssen Nahrung finden, um Energie zu regenerieren und zu überleben.

Die verschiedenen Pflanzen- und Tierarten sind als Unterklassen umgesetzt worden.

---

## 4. Regeln des Ökosystems

### ⚙️ Allgemeines Regelwerk
* Die Simulation läuft in diskreten Runden ab.
* Alle Lebewesen altern um genau eine Einheit pro Runde.
* Lebewesen markieren sich bei Erfüllung der Sterbekriterien selbst als tot, löschen sich jedoch nicht eigenständig aus dem Speicher.
* Tote Lebewesen werden am Ende jeder Runde gesammelt durch das `Habitat` entfernt (Cleanup-Phase).

### 🌱 Regeln für Pflanzen
* Pflanzen besitzen eine minimale und eine maximale Größe.
* Das Wachstum hängt stark von der Pflanzenart und der aktuellen Jahreszeit ab.
* Wird eine Pflanze gefressen, reduziert sich ihre Größe. Fällt die Größe unter die minimale Grenze (`min_size`), stirbt die Pflanze.
* Pflanzen können sich mit einer Wahrscheinlichkeit von **50%** fortpflanzen, sofern sie alt und groß genug sind und ausreichend Platz im Habitat vorhanden ist.
* **Pflanzenarten:**
    * `SummerPlant`: Wächst im Sommer am stärksten.
    * `WinterPlant`: Wächst im Winter am stärksten.
    * `PoisonPlant`: Wächst konstant; kann Allesfresser (`Omnivores`) beim Verzehr vergiften.

### 🦁 Regeln für Tiere
* Tiere verlieren standardmäßig eine Energieeinheit pro Runde.
* **Winterschlaf:** Befinden sich Tiere im Winterschlaf, erleiden sie keinen Energieverlust.
* Tiere müssen erfolgreich fressen, um Energie zu gewinnen. Fällt das Energielevel auf oder unter Null, sterben sie.
* Tiere können sich mit einer Wahrscheinlichkeit von **50%** fortpflanzen, wenn sie das Mindestalter und genug Energie besitzen sowie Platz im Habitat ist.
* **Tierarten:**
    * `Herbivore` (Pflanzenfresser): Frisst ausschließlich Pflanzen.
    * `Carnivore` (Fleischfresser): Jagt und frisst andere Tiere.
    * `Omnivore` (Allesfresser): Frisst Pflanzen und jagt Tiere.

### ⚠️ Spezialregeln
* **Vergiftung:** Wenn ein `Omnivore` eine `PoisonPlant` frisst, besteht eine Chance von **30%**, dass es erhebliche Energie verliert (und eventuell stirbt).
* **Winterschlaf-Bedingung:** Im Winter gehen alle Tiere (Herbivore, Carnivore, Omnivore) in den Winterschlaf, sofern sie genügend Energie besitzen. Haben sie zu wenig Energie, sterben sie direkt. Sobald die Jahreszeit wechselt, wachen alle Überlebenden auf.
* **Jagderfolg:** Der Jagderfolg von `Carnivoren` ist im Herbst durch schlechtere Bedingungen auf **30%** reduziert, in allen anderen Jahreszeiten beträgt er **60%**.
* **Kapazitätsgrenze:** Eine Reproduktion und Wachstum finden nur statt, wenn das `Habitat` noch über freien Platz verfügt.

---

## 5. Rundenablauf

Jede Runde folgt einer strikten, sequentiellen Phasenreihenfolge:

1. **Initialisierung:** Das Event-Log der vorherigen Runde wird geleert.
2. **Pflanzenphase:** Alle lebenden Pflanzen wachsen (wetterabhängig), versuchen sich zu reproduzieren oder sterben.
3. **Tierphase:** Tiere verbrauchen Energie, suchen nach Nahrung (Jagen/Fressen), pflanzen sich bei Erfolg fort oder treten in den Winterschlaf bzw. sterben.
4. **Cleanup-Phase:** Das Habitat filtert alle als tot markierten Objekte heraus.
5. **Logging und Ausgabe:** Die Ereignisse der Runde und der aktuelle Populationsstand werden auf der Konsole ausgegeben.

---

## 6. Zufallskomponenten

Um eine dynamische und unvorhersehbare Ökosystem-Entwicklung zu garantieren, sind folgende Aspekte zufallsbasiert:
* Jagderfolg von Fleisch- und Allesfressern.
* Erfolgschance bei der Fortpflanzung von Pflanzen und Tieren.
* Eintritt der Vergiftung beim Verzehr einer `PoisonPlant`.

---

## 7. Event-Logging

Jede Aktion innerhalb des Habitats erzeugt ein strukturiertes Ereignis, welches getrackt wird, z.B.:
* Wachstum einer Pflanze.
* Fressen einer Pflanze oder eines Tieres.
* Tod eines Lebewesens.
* Wechsel der Jahreszeit.

Am Ende jeder Runde wird eine Übersicht über alle Geschehnisse und den aktuellen Stand (Anzahl Pflanzen/Tiere) ausgegeben.

---

## 8. Benutzerhandbuch (UI)

Die Steuerung und Konfiguration der Simulation erfolgt über die Konsole.

1. Nach dem Start des Programms wird der Benutzer nach einer Startkonfiguration gefragt (Größe des Habitats, Anzahl der Lebewesen).
2. Die `main.py`-Datei enthält das Nutzerprogramm zur Eingabe der Startwerte und die Initialisierung der Simulation. Dazu werden die Klassen aus `ecosystem.py` und die `run_simulation`-Funktion aus `round.py` genutzt.
3. Der Nutzer wird nach dem Platz im Habitat, der Anzahl der Runden der Simulation und der Anzahl der jeweiligen Lebewesen in dem Habitat gefragt. 
4. Bei jeder Nutzereingabe prüft die `ask_number`-Funktion, ob die Eingabe ein valider Integer `>= 0` ist. 
5. Nach der Fertigstellung der Nutzereingaben startet das Programm die Simulation und gibt dabei alle Rundeninformationen und Endinformationen nach Ablauf der angegebenen Runden aus.

---

## 9. Annahmen

* **Alterstod** wird indirekt über den Energieverlust modelliert.
* Alle Lebewesen altern gleichmäßig pro Runde.
* Jahreszeiten wechseln alle zwei Runden in fester Reihenfolge.

---

## 10. Konkrete Werte zu den Regeln

### 🌱 Pflanzen

| Eigenschaft | Wert / Regel |
| :--- | :--- |
| **Startgröße** | 3 |
| **Minimale Größe (`min_size`)** | 3 |
| **Maximale Größe (`max_size`)** | 10 |
| **Reproduktion möglich ab** | Alter > 2 und Größe ≥ 4 |
| **Reproduktionswahrscheinlichkeit** | 50% |
| **SummerPlant Wachstum** | +2 (Sommer), +1 (Frühling/Herbst), +0 (Winter) |
| **WinterPlant Wachstum** | +2 (Winter), sonst +1 |
| **PoisonPlant Wachstum** | +1 immer |
| **Beim Fressen (get_eaten)** | Pflanze verliert pro Biss 1 Größe |

### 🦁 Tiere

| Eigenschaft | Wert / Regel |
| :--- | :--- |
| **Startenergie** | 5 |
| **Energieverlust pro Runde** | -1 (außer beim Schlafen / `sleeping`) |
| **Reproduktion möglich ab** | Alter > 2 und Energie ≥ 6 |
| **Reproduktionswahrscheinlichkeit** | 50% |
| **Herbivore isst erfolgreich** | +2 Energie |
| **Carnivore/Omnivore jagt erfolgreich** | +3 Energie |
| **Herbivore findet Essen** | 70% Chance (Fehlschlag, wenn `random() >= 0.7`) |
| **Omnivore "findet" Essen** | 60% Chance |
| **Carnivore Jagderfolg** | 30% im Herbst, sonst 60% |
| **Winterschlaf-Regel** | Im Winter, wenn Energie ≥ 3: `sleeping`, sonst Tod |
| **PoisonPlant Effekt** | 30% Chance, dann -3 Energie (und ggf. Tod) |

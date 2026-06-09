"""
round.py

Includes the round logic for the simulation and the print_round_summary and
run_simulation function.
"""

__author__ = "8766674, Fehr, 7791598, Schidlauskat"

from ecosystem import (
    Habitat,
    Plant,
    SummerPlant,
    WinterPlant,
    PoisonPlant,
    Animal,
    Herbivore,
    Carnivore,
    Omnivore
)


def run_simulation(habitat: Habitat, max_rounds: int) -> None:
    """
    Runs the ecosystem simulation for a fixed number of rounds.

    :param habitat: Habitat
    :param max_rounds: int
    :return: None

    >>> from ecosystem import Habitat, SummerPlant, Herbivore
    >>> h = Habitat(50)
    >>> h.add_plant(SummerPlant(h.new_id(), "summer_plant"))
    >>> h.add_animal(Herbivore(h.new_id(), "herbivore"))
    >>> run_simulation(h, 1)
    >>> isinstance(h.plants, list)
    True
    >>> isinstance(h.animals, list)
    True
    """
    for current_round in range(1, max_rounds + 1):

        # Events der Runde zurücksetzen
        habitat.clear_events()

        # Alter erhöhen
        for plant in habitat.plants:
            plant.increment_age()

        for animal in habitat.animals:
            animal.increment_age()


        # Pflanzenphase

        new_plants: list[Plant] = []

        for plant in habitat.plants:
            plant.act(habitat)


        # Reproduktion

            if plant.is_alive() and plant.try_reproduce():
                if habitat.has_space(plant.min_size):
                    new_id: int = habitat.new_id()

                    if isinstance(plant, SummerPlant):
                        child = SummerPlant(new_id, plant.species)
                    elif isinstance(plant, WinterPlant):
                        child = WinterPlant(new_id, plant.species)
                    elif isinstance(plant, PoisonPlant):
                        child = PoisonPlant(new_id, plant.species)
                    else:
                        continue

                    new_plants.append(child)

                    habitat.log_event("plant_reproduce", {
                        "parent_id": plant.id,
                        "child_id": child.id,
                        "species": child.species
                    })
                else:
                    habitat.log_event("plant_reproduce_fail", {
                        "parent_id": plant.id,
                        "reason": "no_space"
                    })

        for plant in new_plants:
            habitat.add_plant(plant)


        # Tierphase

        new_animals: list[Animal] = []

        for animal in habitat.animals:
            animal.act(habitat)

            if animal.is_alive() and animal.try_reproduce():
                new_id: int = habitat.new_id()

                if isinstance(animal, Herbivore):
                    child = Herbivore(new_id, animal.species)
                elif isinstance(animal, Carnivore):
                    child = Carnivore(new_id, animal.species)
                elif isinstance(animal, Omnivore):
                    child = Omnivore(new_id, animal.species)
                else:
                    continue

                new_animals.append(child)

                habitat.log_event("animal_reproduce", {
                    "parent_id": animal.id,
                    "child_id": child.id,
                    "species": child.species
                })

        for animal in new_animals:
            habitat.add_animal(animal)


        # Cleanup

        habitat.cleanup()


        # Saisonwechsel

        if current_round % 2 == 0:
            habitat.change_season()


        # Ausgabe

        print_round_summary(current_round, habitat)


def print_round_summary(round_number: int, habitat: Habitat) -> None:
    """
    Prints a compact summary of a simulation round.

    :param round_number: int
    :param habitat: Habitat
    :return: None

    >>> from ecosystem import Habitat
    >>> h = Habitat(10)
    >>> print_round_summary(1, h)
    """

    print("\n____________________________")
    print(f"Runde {round_number}")
    print(f"Saison: {habitat.season}")
    print(f"Pflanzen: {len(habitat.plants)} , Tiere: {len(habitat.animals)}")

    if habitat.event_log:
        print("Ereignisse:")
        for event in habitat.event_log:
            print(f" - {event['type']}: {event['information']}")
    else:
        print("Keine Ereignisse.")

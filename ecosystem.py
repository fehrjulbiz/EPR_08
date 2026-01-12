"""
This Module holds the ecosystem Class and all the living_beings as subclasses
in this ecosystem.
"""

from random import random

## Main Living Being Class

class LivingBeing:
    def __init__(self, id_number, species):
        self.id = id_number
        self.energy = 2
        self.age = 1
        self.condition = "alive"
        self.species = species





## Plant Parent Class

class Plant(LivingBeing):
    def __init__(self, id_number, species):
        super().__init__(id_number,species)
        self.size = self.energy = 3  # energy for plant is size but starts
        # with 3
        self.min_size = 3

    def increment_age(self):
        self.age += 1


    def try_reproduce(self):
        if self.age >= 3 and self.energy >= 4:
            return True
        else:
            return False


    def die(self):
        self.condition = "dead"


## Plant Subclasses

class SummerPlant(Plant):

    def __init__(self, id_number, species):
        super().__init__(id_number,species)




class WinterPlant(Plant):

    def __init__(self, id_number, species):
        super().__init__(id_number,species)




class PoisonPlant(Plant):

    def __init__(self, id_number, species):
        super().__init__(id_number,species)


    def interact(self):
        pass










## Animal Parent Class

class Animal(LivingBeing):
    def __init__(self, id_number, species):
        super().__init__(id_number,species)
        self.age = self.age


    def increment_age(self):
        self.age += 1


    def try_reproduce(self):
        if self.age >= 3 and self.energy >= 4:
            return True
        else:
            return False



## Animal Subclasses

class Carnivore(Animal):
    def __init__(self, id_number, species):
        super().__init__(id_number,species)

    def interact(self):
        pass

class Herbivore(Animal):
    def __init__(self, id_number, species):
        super().__init__(id_number,species)

    def interact(self):
        pass


class Omnivore(Animal):
    def __init__(self, id_number, species):
        super().__init__(id_number,species)


    def interact(self):
        pass




## Habitat Class

class Habitat:
    seasons = {"summer": "autumn", "autumn": "winter", "winter": "spring",
               "spring": "summer"}

    def __init__(self, space):
        self.space = int(space)
        self.season = "spring"  # habitat startet im frühling
        self.entity_count = {"plants": 0, "animals": 0}
        self.species_count = {"summer_plant": 0, "winter_plant": 0,
                              "poison_plant": 0, "herbivore": 0, "omnivore": 0
                              , "carnivore": 0}
        self.animals = []
        self.plants = []


    def change_season(self):
        self.season = self.seasons.get(self.season)

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def add_plant(self, plant: Plant):
        self.plants.append(plant)

    def clean_habitat(self):

        alive_animals = []
        for animal in self.animals:
            if animal.condition != "dead":
                alive_animals.append(animal)
            else:
                self.species_count[animal.species] -= 1
                self.entity_count["animals"] -= 1
        self.animals = alive_animals

        alive_plants = []
        for plant in self.plants:
            if plant.condition != "dead":
                alive_plants.append(plant)
            else:
                self.species_count[plant.species] -= 1
                self.entity_count["plants"] -= 1
        self.plants = alive_plants





        for animal in self.animals[:]:  # über kopie iterieren, da wir die
            # Liste verändern. Sonst könnten elemente übersprungen werden.
            if animal.condition == "dead":
                self.animals.remove(animal)
                self.entity_count["animals"] -= 1
                self.species_count[animal.species] -= 1




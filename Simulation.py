import random
from SimData import SimData
from Defaults import Defaults
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass

class SimulationClass:
    def __init__(self, name):
        self.name = name
        self.config = SimData.getSimByName(name)
        self.world = self.initWorld()
        
    def initWorld(self):
        #World
        world = WorldClass(self.config["world"])

        #Villages
        for villageSettings in self.config["villages"]:
            village = VillageClass(villageSettings)

            #Villagers
            for vType in world.startingVillagers:
                villager = VillagerClass(vType, self.config["villagers"][vType])
                village.addVillager(villager)            
        
            #Locations
            for lType in village.startingLocations:
                location = LocationClass(lType, self.config['locations'][lType])
                village.addLocation(location)
            
            #Buildings
            for bType in village.startingBuildings:
                building = BuildingClass(bType, self.config['buildings'][bType])
                location = village.findLocationForBuilding(bType)
                village.addBuilding(building, location)
            
            world.addVillage(village) 
            
        return world
    
if __name__ == '__main__':
    from pprint import pprint 
    sim = SimulationClass("The Myst")
    pprint(sim.__dict__)
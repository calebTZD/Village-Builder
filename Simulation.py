import random
from SimData import SimData
from Defaults import Defaults
from Config import ConfigClass
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass

class SimulationClass:
    def __init__(self, name):
        self.name = name
        config = SimData.getSimByName(name)
        self.config = ConfigClass(config)
        self.world = self.initWorld()
        
    def initWorld(self):
        #World
        world = WorldClass(self.config.world)

        #Villages
        for villageName in self.config.villages:
            village = VillageClass(self.config.villages[villageName])

            #Villagers
            for vType in world.startingVillagers:
                self.createVillager(vType, village)      
        
            #Locations
            for lType in village.startingLocations:
                self.createLocation(lType, village)
            
            #Buildings
            for bType in village.startingBuildings:
                self.createBuilding(bType, village)
            
            world.addVillage(village) 
            
        return world

    def createVillager(self, vType, village):
        villager = VillagerClass(vType, self.config.villagers[vType])
        village.addVillager(villager)

    def createLocation(self, lType, village):
        location = LocationClass(lType, self.config.locations[lType])
        village.addLocation(location)
    
    def createBuilding(self, bType, village):
        building = BuildingClass(bType, self.config.buildings[bType])
        location = village.findLocationForBuilding(bType)
        village.addBuilding(building, location)



if __name__ == '__main__':
    from pprint import pprint 
    sim = SimulationClass("The Myst")
    pprint(sim.__dict__)
    pprint(sim.config.__dict__)
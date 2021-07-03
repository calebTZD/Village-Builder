import random
from SimData import SimData
from Defaults import Defaults
from Config import ConfigClass
from World import WorldClass
from Villager import VillagerClass
from Village import VillageClass
from Building import BuildingClass
from Location import LocationClass
from Stats import SimStatsClass

class SimulationClass:
    def __init__(self, name):
        self.name = name
        config = SimData.getSimByName(name)
        self.config = ConfigClass(config)
        self.world = self.initWorld()
        self.stats = SimStatsClass(self)

    def toDict(self):
        return self.stats.statDict()       

    def initWorld(self):
        #World
        world = WorldClass(self, self.config.world)

        #Villages
        for villageName in self.config.villages:
            village = VillageClass(world, self.config.villages[villageName])

            #Villagers
            for vType in world.startingVillagers:
                village.addVillager(vType)      
        
            #Locations
            for lType in village.startingLocations:
                village.addLocation(lType)
            
            #Buildings
            for bType in village.startingBuildings:
                village.addBuilding(bType)
            
            world.addVillage(village) 
            
        return world
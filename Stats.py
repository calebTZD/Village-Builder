from util import *


class SimStatsClass:
    def __init__(self, sim):
        self.sim = sim
        self.ticks = 0

    def statDict(self):
        stats = {
            'ticks': self.ticks,
            'world': self.sim.world.toDict()
        }

class WorldStatsClass:
    def __init__(self, world):
        self.world = world

    def statDict(self):
        stats = {
            'days': self.world.days,
            'numVillages': self.world.numVillages,
            'maxVillagersPerVillage': self.world.maxVillagersPerVillage,
            'numVillages': self.world.numVillages
        }
        stats['villages'] = []
        for village in self.world.villages:
            stats['villages'].append(village.toDict())

class VillageStatsClass:
    def __init__(self, village):
        self.village = village
        self.timesAttacked = 0
        self.timesToWar = 0
        self.enemyBuildingsDestroed = 0
        self.enemyKilled = 0
        self.damageOutput = 0
        self.damageInput = 0 

    def statDict(self):
        stats = {
            'name': self.village.name,
            'timesAttacked': self.timesAttacked
        }
        stats['villagerCount'] = {}
        for vType in V_Type:
            stats['villagerCount'][vType.value] = len(self.village.getVillagersByType(vType.value))
        stats['villagers'] = []
        for villager in self.village.villagers:
            stats['villagers'].append(villager.toDict())
        stats['buildingCount'] = {}
        for bType in B_Type:
            stats['buildingCount'][bType.value] = len(self.village.getBuildingsByType(bType.value))
        stats['locations'] = []
        for location in self.village.locations:
            stats['locations'].append(location.toDict())
        stats['buildings'] = []
        for building in self.village.buildings:
            stats['buildings'].append(building.toDict())
        stats['resources'] = {}
        for rType in R_Type:
            stats['resources'][rType.value] = self.village.resources[rType.value]
        stats['destroyedBuildings'] = len(self.village.destroyed)
        stats['deadVillagers'] = len(self.village.dead)

        return stats

class VillagerStatsClass:
    def __init__(self, villager):
        self.villager = villager
        self.harvestedResources = {}
        for rType in R_Type:
           self.harvestedResources[rType.value] = 0

    def statDict(self):
        stats = {
            'type': self.villager.type,
            'level': self.villager.getLevel(),
            'harvestedResources': dict(self.harvestedResources)
        }
        return stats

class LocationStatsClass:
    def __init__(self, location):
        self.location = location

    def statDict(self):
        stats = {
            'type': self.location.type
        }
        return stats

class BuildingsStatsClass:
    def __init__(self, building):
        self.building = building

    def statDict(self):
        stats = {
            'type': self.building.type
        }
        return stats
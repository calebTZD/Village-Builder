from util import *
import datetime

class SimStatsClass:
    def __init__(self, sim):
        self.sim = sim
        self.tickStats = {}
        self.ticks = 0

    def statDict(self):
        stats = {            
            'simName': self.sim.name,
            'config': self.sim.config.toDict(),
            'ticks': self.ticks,
            'tickStats': self.tickStats,
            'world': self.sim.world.toDict()
        }
        stats['timeStamp'] = self.getTime()
        return stats

    def doTickStats(self):
        self.sim.world.stats.doTickStats()

    def getTime(self):
        fTime = datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%S")
        return fTime

class WorldStatsClass:
    def __init__(self, world):
        self.world = world
        self.tickStats = {}


    def statDict(self):
        stats = {
            'days': self.world.days,
            'tickStats': self.tickStats,
            'numVillages': self.world.numVillages,
            'maxVillagersPerVillage': self.world.maxVillagersPerVillage,
        }
        stats['villages'] = []
        for village in self.world.villages:
            stats['villages'].append(village.toDict())
        return stats

    def doTickStats(self):
        for village in self.world.villages:
            village.stats.doTickStats()

class VillageStatsClass:
    def __init__(self, village):
        self.village = village
        self.tickStats = {}
        self.initTickStats()
        self.timesAttacked = 0
        self.timesToWar = 0
        self.enemyBuildingsDestroed = 0
        self.enemyKilled = 0
        self.damageOutput = 0
        self.damageInput = 0 
        # self.score = village.getScore()

    def initTickStats(self):
        self.tickStats['resources'] = {}
        for rType in R_Type:
            self.tickStats['resources'][rType.value] = []

        self.tickStats['villagers'] = {}
        for vType in V_Type:
            self.tickStats['villagers'][vType.value] = []

        self.tickStats['buildings'] = {}
        for bType in B_Type:
            self.tickStats['buildings'][bType.value] = []

    def statDict(self):
        stats = {
            'name': self.village.name,
            'tickStats': self.tickStats,
            'timesAttacked': self.timesAttacked,
            'timesToWar': self.timesToWar,
            'enemyBuildingsDestroed': self.enemyBuildingsDestroed,
            'enemyKilled': self.enemyKilled,
            'damageOutput': self.damageOutput,
            'damageInput': self.damageInput,
            # 'score': self.score,
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

    def doTickStats(self):
        for villager in self.village.villagers:
            villager.stats.doTickStats()
        for location in self.village.locations:
            location.stats.doTickStats()
        for building in self.village.buildings:
            building.stats.doTickStats()
        
        for rType in R_Type:
            self.tickStats['resources'][rType.value].append(self.village.resources[rType.value])
        for vType in V_Type:
            self.tickStats['villagers'][vType.value].append(len(self.village.getVillagersByType(vType.value)))
        for bType in B_Type:
            self.tickStats['buildings'][bType.value].append(len(self.village.getBuildingsByType(bType.value)))

class VillagerStatsClass:
    def __init__(self, villager):
        self.villager = villager
        self.tickStats = {}
        self.harvestedResources = {}
        for rType in R_Type:
           self.harvestedResources[rType.value] = 0

    def statDict(self):
        stats = {
            'type': self.villager.type,
            'level': self.villager.getLevel(),
            'tickStats': self.tickStats,
            'harvestedResources': dict(self.harvestedResources)
        }
        return stats

    def doTickStats(self):
        pass

class LocationStatsClass:
    def __init__(self, location):
        self.location = location
        self.tickStats = {}

    def statDict(self):
        stats = {
            'type': self.location.type,
            'tickStats': self.tickStats
        }
        return stats

    def doTickStats(self):
        pass

class BuildingsStatsClass:
    def __init__(self, building):
        self.building = building
        self.tickStats = {}

    def statDict(self):
        stats = {
            'type': self.building.type,
            'tickStats': self.tickStats
        }
        return stats

    def doTickStats(self):
        pass
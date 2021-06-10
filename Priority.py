import re
from Defaults import Defaults
from random import shuffle
from util import *

BUILDING_MULTIPLIER = 5
VILLAGER_MULTIPLIER = 1
RESOURCE_MULTIPLIER = 1

class PRIORITIES(Enum):
    FOOD = "Food"
    WOOD = "Wood"
    STONE = "Stone"
    ORE = "Ore"
    GOLD = "Gold"
    ATTACK = "Attack"
    DEFENSE = "Defense"
    RESEARCH = "Research"
    EXPLORE = "Exploring"

VILLAGER_PRIORITY_MAP = {
    V_Type.FARMER.value: "FOOD",
    V_Type.HUNTER.value: "FOOD",    
    V_Type.LUMBERJACK.value: "WOOD",
    V_Type.STONEMASON.value: "STONE",
    V_Type.MINER.value: "ORE",
    V_Type.MERCHANT.value: "GOLD",
    V_Type.WARRIOR.value: "ATTACK",
    V_Type.GUARD.value: "DEFENSE",
    V_Type.RESEARCHER.value: "RESEARCH",
    V_Type.SCOUT.value: "EXPLORE"
}

BUILDING_PRIORITY_MAP = {
    B_Type.FARM.value: "FOOD",
    B_Type.HUNTINGHUT.value: "FOOD",    
    B_Type.LOGGINGCAMP.value: "WOOD",
    B_Type.QUARRY.value: "STONE",
    B_Type.MINE.value: "ORE",
    B_Type.MARKET.value: "GOLD",
    B_Type.BARRACKS.value: "WAR",
    B_Type.LIBRARY.value: "RESEARCH",
    B_Type.TOWNHALL.value: "FOOD"
}

class PriorityClass:
    def __init__(self):
        self.rotationPriorities = {}

    def getRandomPriority(self, village):
        priorityList = list(village.priorities.keys())
        shuffle(priorityList)
        return priorityList

    def getRotationPriority(self, village):
        if not village.name in self.rotationPriorities:
            tempPriorities = dict(village.priorities)
            tempPriorities = {k: v for k, v in sorted(tempPriorities.items(), key=lambda item: item[1], reverse=True)}
            self.rotationPriorities[village.name] = list(tempPriorities.keys())            
        else:
            self.rotationPriorities[village.name].append(self.rotationPriorities[village.name].pop(0))
        return self.rotationPriorities[village.name]
    
    def getVillagePriorityValues(self, village):
        priorities = {}
        for p in PRIORITIES:
            priorities[p.value] = 0

        for villager in village.villagers:
            priority = VILLAGER_PRIORITY_MAP[villager.type]
            priorities[PRIORITIES[priority].value] += 1*VILLAGER_MULTIPLIER

        for building in village.buildings:
            priority = BUILDING_PRIORITY_MAP[building.type]
            priorities[PRIORITIES[priority].value] += 1*BUILDING_MULTIPLIER
        return priorities
    
    def calcVillageDiff(self, village):
        priorities = [PRIORITIES.FOOD.value, PRIORITIES.WOOD.value, PRIORITIES.STONE.value, PRIORITIES.ORE.value, PRIORITIES.GOLD.value, PRIORITIES.ATTACK.value, PRIORITIES.DEFENSE.value, PRIORITIES.RESEARCH.value]
        configSet = village.priorities
        currSet = self.getVillagePriorityValues(village)
        return self.calcPDiff(priorities, configSet, currSet)   

    def calcResourcesDiff(self, village):
        priorities = [PRIORITIES.FOOD.value, PRIORITIES.WOOD.value, PRIORITIES.STONE.value, PRIORITIES.ORE.value, PRIORITIES.GOLD.value, PRIORITIES.RESEARCH.value]
        configSet = village.priorities
        currSet = village.resources
        return self.calcPDiff(priorities, configSet, currSet)

    def calcPDiff(self, priorities, configSet, currSet):
        #Resource percentages from configuration
        configTotal = 0
        currTotal = 0
        for priority in priorities:
            configTotal += configSet[priority]
            currTotal += currSet[priority]
        
        diff = {}
        for priority in priorities:
            configPercent = round(configSet[priority]/configTotal*100)
            currPercent = round(currSet[priority]/currTotal*100)
            diff[priority] = configPercent - currPercent
        return diff

    def calcPriorities(self, village):
        vDiff = Priority.calcVillageDiff(self.village)
        print(diff)
        rDiff = Priority.calcResourcesDiff(self.village)
        print(diff)
        for priority in rDiff:

Priority = PriorityClass()

if __name__ == '__main__':
    from pprint import pprint 
    from Village import VillageClass  
    villageSettings = Defaults.simulation["villages"][0]
    village = VillageClass(villageSettings)
    Priority.calcPriorities(village)
    # print(village.priorities)
    # print(P.getRandomPriority(village))
    # print(P.getRandomPriority(village))
    # print(P.getRotationPriority(village))
    # print(P.getRotationPriority(village))
    # print(P.getRotationPriority(village))
    # print(P.getRotationPriority(village))



from Simulation import SimulationClass
import re
from Defaults import Defaults
from random import shuffle
from util import *

BUILDING_MULTIPLIER = 50
VILLAGER_MULTIPLIER = 10
RESOURCE_MULTIPLIER = 1
WARRIOR_MULTIPLIER = 20

class PRIORITIES(Enum):
    FOOD = "Food"
    WOOD = "Wood"
    STONE = "Stone"
    ORE = "Ore"
    GOLD = "Gold"
    ATTACK = "Attack"
    DEFENSE = "Defense"
    PROJECTX = "ProjectX"
    RESEARCH = "Research"
    EXPLORE = "Exploring"

VILLAGER_PRIORITY_MAP = {
    V_Type.FARMER.value: "FOOD",    
    V_Type.LUMBERJACK.value: "WOOD",
    V_Type.STONEMASON.value: "STONE",
    V_Type.MINER.value: "ORE",
    V_Type.MERCHANT.value: "GOLD",
    V_Type.WARRIOR.value: "ATTACK",
    V_Type.GUARD.value: "DEFENSE",
    V_Type.RESEARCHER.value: "RESEARCH",
    V_Type.DRX.value: "PROJECTX",
    V_Type.SCOUT.value: "EXPLORE"
}
PRIORITY_VILLAGER_MAP = {
    "Food": V_Type.FARMER.value,
    "Wood": V_Type.LUMBERJACK.value,
    "Stone": V_Type.STONEMASON.value,
    "Ore": V_Type.MINER.value,
    "Gold": V_Type.MERCHANT.value,
    "Attack": V_Type.WARRIOR.value,
    "Defense": V_Type.GUARD.value,
    "Research": V_Type.RESEARCHER.value,
    "ProjectX": V_Type.DRX.value,
    "Explore": V_Type.SCOUT.value
}

BUILDING_PRIORITY_MAP = {
    B_Type.FARM.value: "FOOD",   
    B_Type.LOGGINGCAMP.value: "WOOD",
    B_Type.QUARRY.value: "STONE",
    B_Type.MINE.value: "ORE",
    B_Type.MARKET.value: "GOLD",
    B_Type.BARRACKS.value: "DEFENSE",
    B_Type.BUILDINGX.value: "PROJECTX",
    B_Type.LIBRARY.value: "RESEARCH",
    B_Type.TOWNHALL.value: "FOOD"
}

RESOURCE_PRIORITY_LIST = [PRIORITIES.FOOD.value, PRIORITIES.WOOD.value, PRIORITIES.STONE.value, \
                          PRIORITIES.ORE.value, PRIORITIES.GOLD.value, PRIORITIES.PROJECTX.value, \
                          PRIORITIES.RESEARCH.value]
VILLAGE_PRIORITY_LIST = [PRIORITIES.FOOD.value, PRIORITIES.WOOD.value, PRIORITIES.STONE.value, \
                         PRIORITIES.ORE.value, PRIORITIES.GOLD.value, \
                         PRIORITIES.DEFENSE.value, PRIORITIES.ATTACK.value, PRIORITIES.PROJECTX.value, PRIORITIES.RESEARCH.value]

class PriorityManagerClass:
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
            if villager.type == V_Type.WARRIOR.value: #Make up for warriors not having buildings
                priorities[PRIORITIES[priority].value] += 1 * WARRIOR_MULTIPLIER
            else:
                priorities[PRIORITIES[priority].value] += 1 * VILLAGER_MULTIPLIER

        for building in village.buildings:
            priority = BUILDING_PRIORITY_MAP[building.type]
            priorities[PRIORITIES[priority].value] += 1*BUILDING_MULTIPLIER
        return priorities
    
    def calcVillageDiff(self, village):
        priorities = VILLAGE_PRIORITY_LIST
        configSet = village.priorities
        currSet = self.getVillagePriorityValues(village)
        return self.calcPriorityDiff(priorities, configSet, currSet)   

    def calcResourcesDiff(self, village):
        priorities = RESOURCE_PRIORITY_LIST
        configSet = village.priorities
        currSet = village.resources
        return self.calcPriorityDiff(priorities, configSet, currSet)

    def calcPriorityDiff(self, priorities, configSet, currSet):
        #Resource percentages from configuration
        configTotal = 0
        currTotal = 0
        for priority in priorities:
            configTotal += configSet[priority]
            currTotal += currSet[priority]
        
        diff = {}
        for priority in priorities:
            configPercent = 0 if configTotal == 0 else round(configSet[priority]/configTotal*100)
            currPercent = 0 if currTotal == 0 else round(currSet[priority]/currTotal*100)
            diff[priority] = configPercent - currPercent
        return diff

    def calcPriorities(self, village):
        vDiff = self.calcVillageDiff(village)
        rDiff = self.calcResourcesDiff(village)
        for priority in rDiff:
            vDiff[priority] += rDiff[priority]*RESOURCE_MULTIPLIER
        return vDiff

    def getTopBottomVillagers(self, village):
        topValue = None
        topPriority = None
        bottomValue = None
        bottomPriority = None
        priorities = self.calcPriorities(village)
        for priority in priorities:
            if (topValue == None) or \
               (topValue < priorities[priority]) or \
               (topValue == priorities[priority] and village.priorities[priority] > village.priorities[topPriority]):
                topPriority = priority
                topValue = priorities[priority]
            
            if (len(village.getVillagersByType(PRIORITY_VILLAGER_MAP[priority])) > 1) and \
               ((bottomValue == None) or \
                (bottomValue > priorities[priority]) or \
                (bottomValue == priorities[priority] and village.priorities[priority] > village.priorities[bottomPriority])):
                bottomPriority = priority
                bottomValue = priorities[priority]
        return topValue, topPriority, bottomPriority

    def whichVillagerToCreate(self, village):
        (topValue, topPriority, bottomPriority) = self.getTopBottomVillagers(village)
        return PRIORITY_VILLAGER_MAP[topPriority]

    def whichVillagerToSwitch(self, village):
        (topValue, topPriority, bottomPriority) = self.getTopBottomVillagers(village)
        topType = PRIORITY_VILLAGER_MAP[topPriority]
        bottomType = None if bottomPriority == None else PRIORITY_VILLAGER_MAP[bottomPriority]
        return topValue, topType, bottomType

    def whichVillagerToUpgrade(self, village):
        levelMod = dict(village.levelMod)
        levelMod.pop('DrX', None)
        lowestLevel = village.levelMod[min(levelMod, key=levelMod.get)]
        sortedPriorities = dict(village.priorities)
        {k: v for k, v in sorted(sortedPriorities.items(), key=lambda item: item[1])}
        for k in sortedPriorities:
            priorityVillager = PRIORITY_VILLAGER_MAP[k]
            if village.levelMod[priorityVillager] == lowestLevel:
                return priorityVillager
import logging

LOGIT = logging.getLogger("Sim_Log")
LOGIT.setLevel(logging.DEBUG)
consoleLog = logging.StreamHandler()
consoleLog.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s][%(filename)s]: %(message)s')
consoleLog.setFormatter(formatter)
LOGIT.addHandler(consoleLog)

from enum import Enum
class V_Status(Enum):
    UNASSIGNED = 1
    TO_LOCATION = 2    
    BUILDING = 3
    HARVESTING = 4
    TO_VILLAGE = 5
    ATTACKING = 6
    SEARCHING = 7
    DEAD = 8
    TO_WAR = 9
    DEFENDING = 10

class V_Type(Enum):
    FARMER = "Farmer"
    LUMBERJACK = "Lumberjack"
    STONEMASON = "Stonemason"
    MINER = "Miner"
    WARRIOR = "Warrior"
    GUARD = "Guard"
    MERCHANT = "Merchant"
    SCOUT = "Scout"
    RESEARCHER = "Researcher"
    DRX = "DrX"

class B_Type(Enum):
    FARM = "Farm"
    LOGGINGCAMP = "LoggingCamp"
    MINE = "Mine"
    QUARRY = "Quarry"
    MARKET = "Market"
    LIBRARY = "Library"
    BARRACKS = "Barracks"
    BUILDINGX = "BuildingX"
    TOWNHALL = "Townhall"

class R_Type(Enum):
    FOOD = "Food"
    WOOD = "Wood"
    STONE = "Stone"
    ORE = "Ore"
    GOLD = "Gold"
    PROJECTX = "ProjectX"
    RESEARCH = "Research"

class L_Type(Enum):
    GRASSLAND = "Grassland"
    FORREST = "Forest"
    OREDEPOSIT = "OreDeposit"
    STONEDEPOSIT = "StoneDeposit"
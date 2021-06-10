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


class V_Type(Enum):
    FARMER = "Farmer"
    LUMBERJACK = "Lumberjack"
    STONEMASON = "Stonemason"
    MINER = "Miner"
    HUNTER = "Hunter"
    WARRIOR = "Warrior"
    GUARD = "Guard"
    MERCHANT = "Merchant"
    SCOUT = "Scout"
    RESEARCHER = "Researcher"

class B_Type(Enum):
    FARM = "Farm"
    LOGGINGCAMP = "LoggingCamp"
    MINE = "Mine"
    QUARRY = "Quarry"
    HUNTINGHUT = "HuntingHut"
    MARKET = "Market"
    LIBRARY = "Library"
    BARRACKS = "Barracks"
    TOWNHALL = "Townhall"
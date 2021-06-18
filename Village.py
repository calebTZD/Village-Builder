from Defaults import Defaults
import util
from Villager import VillagerClass
from Location import LocationClass
from Building import BuildingClass
from Stats import VillageStatsClass

class VillageClass:
    def __init__(self, world, settings):
        self.world = world
        self.initSettings(settings)

        #Initial Values
        self.locations = []
        self.buildings = []
        self.villagers = []
        self.enemyVilages = []
        self.dead = []
        self.destroyed =[]
        self.levelMod = {
            "Farmer": 1,
            "Lumberjack": 1,
            "Miner": 1,
            "Stonemason": 1,
            "Merchant": 1,
            "Warrior": 1,
            "Guard": 1,
            "Scout": 1,
            "DrX": 1,
            "Researcher": 1
        }

        #Stats
        self.stats = VillageStatsClass(self)

    def toDict(self):
        return self.stats.statDict()

    def initSettings(self, settings):
        self.startingLocations = settings["startingLocations"]
        self.startingBuildings = settings["startingBuildings"]
        self.name = settings["name"]
        self.priorities = settings["priorities"]
        #TODO Add resources to default data and UI
        self.resources = {
            "Food": 0,
            "Wood": 0,
            "Stone": 0,
            "Ore": 0,
            "Gold": 0,
            "ProjectX": 0,
            "Research": 0
        }

    def getVillagersByType(self, type):
        villagers = []
        for villager in self.villagers:
            if villager.type == type:
                villagers.append(villager)
        return villagers

    def addVillager(self, vType):
        villager = VillagerClass(vType, self.world.sim.config.villagers[vType])
        self.villagers.append(villager)
        villager.village = self

    def addBuilding(self, bType):
        building = BuildingClass(bType, self.world.sim.config.buildings[bType])
        location = self.findLocationForBuilding(bType)
        location.addBuilding(building)
        self.buildings.append(building)
        building.village = self

    def addLocation(self, lType):
        location = LocationClass(lType, self.world.sim.config.locations[lType])
        self.locations.append(location)
        location.village = self
    
    def incResource(self, resourceType, amount):
        self.resources[resourceType] += amount

    def findLocationForBuilding(self, bType):
        for location in self.locations:
            if bType in location.buildingTypes and len(location.buildings) < location.maxBuildings:
                return location

    def canBuild(self, type):
        cost = Defaults.buildingsConfig[type]["cost"]
        for resource in cost:
            for reso in self.resources:
                if resource == reso:
                    if self.resources[reso] < cost[resource]:
                        return False
        return True

    def canCreate(self, cost):        
        for resource in cost:
            for reso in self.resources:
                if resource == reso:
                    if self.resources[reso] < cost[resource]:
                        return False
        return True

    def build(self, type):
        # take resources away from village
        cost = Defaults.buildingsConfig[type]["cost"]
        for resource in cost:
            for reso in self.resources:
                if resource == reso:
                    self.resources[reso] -= cost[resource]

    def spend(self, cost):
        # take resources away from village        
        for resource in cost:
            for reso in self.resources:
                if resource == reso:
                    self.resources[reso] -= cost[resource]

    def addEnemy(self, village):
        if not village in self.enemyVilages:
            self.enemyVilages.append(village)

    def underAttack(self):
        for building in self.buildings:
            if building.enemyPresent():
                
                return building
        return None

    def switchVillagers(self, top, bottom):
        for villager in self.villagers:
            if villager.type != bottom:
                continue
            else:
                villager.depositLoad()
                villager.type = top
                villager.status = util.V_Status.UNASSIGNED
                villager.initSettings(self.world.sim.config.villagers[villager.type])
                return

    def attacking(self):
        for villager in self.villagers:
            if villager.type == "Warrior":
                for building in self.buildings:
                    if building == villager.assignedBuilding:
                        break
                return True
        return False
        

    
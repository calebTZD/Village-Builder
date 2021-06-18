from util import V_Status
from Defaults import Defaults
from Stats import BuildingsStatsClass

class BuildingClass:
    def __init__(self, bType, buildingSettings):
        self.type = bType
        self.initSettings(buildingSettings)

        #Initial Values
        self.village = None
        self.location = None
        self.currentHealth = int(self.maxHealth)
        self.buildTimeLeft = self.buildTime
        self.currentResources = int(self.resourceAmount)
        self.villagers = []
        self.enemies = []

        #Stats
        self.stats = BuildingsStatsClass(self)

    def toDict(self):
        return self.stats.statDict()

    def initSettings(self, buildingSettings):
        self.cost = buildingSettings["cost"]
        self.villagersAbleToSupport = buildingSettings["villagersAbleToSupport"]
        self.resource = buildingSettings["resource"]
        self.enhancemntFactor = buildingSettings["enhancemntFactor"]
        self.maxHealth = buildingSettings["maxHealth"]
        self.buildTime = buildingSettings["buildTime"]
        self.resourceAmount = buildingSettings["resourceAmount"]
        self.enhancemntCost = buildingSettings["enhancemntCost"]        

    def assignVillager(self, villager):
        self.villagers.append(villager)
        villager.assignedBuilding = self

    def enemyPresent(self):
        if len(self.enemies) > 0:
            return True
        return False

    def attacked(self, villager):
        self.currentHealth -= villager.calcAttack()
        if self.currentHealth <= 0:
            self.village.destroyed.append(self)
            self.village.buildings.pop(self)
            for villager in self.villagers:
                villager.status = V_Status.UNASSIGNED
                villager.assignedBuilding = None
                self.villagers.pop(villager)
            self.enemies = []


if __name__ == '__main__':    
    from pprint import pprint
    from Location import LocationClass
    location = LocationClass('Grassland', Defaults.simulation["locations"]["Grassland"])    
    for bType, buildingSettings in Defaults.simulation["buildings"].items():
        b = BuildingClass(bType, buildingSettings)
        location.addBuilding(b)
        pprint(b.__dict__)
        pprint(b.location.__dict__)
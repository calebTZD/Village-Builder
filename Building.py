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
        self.villagersAbleToSupport = int(buildingSettings["villagersAbleToSupport"])
        self.resource = buildingSettings["resource"]
        self.enhancemntFactor = int(buildingSettings["enhancemntFactor"])
        self.maxHealth = int(buildingSettings["maxHealth"])
        self.buildTime = int(buildingSettings["buildTime"])
        self.resourceAmount = int(buildingSettings["resourceAmount"])
        self.enhancemntCost = int(buildingSettings["enhancemntCost"])       

    def assignVillager(self, villager):
        self.villagers.append(villager)
        villager.assignedBuilding = self

    def enemyPresent(self):
        if len(self.enemies) > 0:
            return True
        return False

    def attacked(self, villager):
        self.currentHealth -= villager.calcAttack()
        villager.village.stats.damageOutput += villager.calcAttack()
        self.village.stats.damageInput += villager.calcAttack()
        if self.currentHealth <= 0:
            villager.village.stats.enemyBuildingsDestroed += 1
            self.village.destroyed.append(self)
            self.village.buildings.remove(self)
            for villager in self.villagers:
                villager.status = V_Status.UNASSIGNED
                villager.assignedBuilding = None
                self.villagers.remove(villager)
            for enemy in self.enemies:
                enemy.findTarget()
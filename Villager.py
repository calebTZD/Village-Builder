from Defaults import Defaults
from util import V_Status
import random

class VillagerClass:
    def __init__(self, vType, villagerSettings):
        self.type = vType

        #Defaults
        self.enhancemntFactor = Defaults.villagersConfig[self.type]["enhancemntFactor"]
        self.preferredBuilding = Defaults.villagersConfig[self.type]["preferredBuilding"]

        #Settings
        self.speed = villagerSettings["speed"]
        self.maxHealth = villagerSettings["maxHealth"]
        self.carryCapacity = villagerSettings["carryCapacity"]
        self.attack = villagerSettings["attack"]
        self.defense = villagerSettings["defense"]
        self.productionSpeed = villagerSettings["productionSpeed"]
        self.spawnTime = villagerSettings["spawnTime"]
        self.enhancemntCost = villagerSettings["enhancemntCost"]
        self.spawnCost = villagerSettings["spawnCost"]

        #Initial Values
        self.village = None
        self.status = V_Status.UNASSIGNED
        self.currentHealth = int(self.maxHealth)
        self.currentLoad = {"": 0}
        self.distance = 0
        self.gatheringType = ""
        self.assignedBuilding = None

        #Stats
        self.stats = {}

    def findBuilding(self):
        self.assignedBuilding = None
        for building in self.village.buildings:
            if building.type == self.preferredBuilding:
                if building.villagersAbleToSupport < len(building.villagers):
                    building.assignVillager(self)
                    self.distance = building.location.distance
        if self.assignedBuilding == None:
            return False
        return True


    def build(self, building):
        self.village.build(self.preferredBuilding)
        # add building to village
        location = self.village.findLocationForBuilding(self.preferredBuilding)
        self.village.addBuilding(building, location)
        self.assignedBuilding = building

    def attacking(self):
        if len(self.assignedBuilding.villagers) >= 0:
            target = self.building.villagers[0]
            target.currentHealth -= self.attack
            self.currentHealth -= target.defense
            if target.currentHealth <= 0:
                target.status = V_Status.DEAD
        else:
            self.building.currentHealth -= self.attack
            
    def findTarget(self):
        target = self.village.enemies[0]
        targets = list(target.buildings)
        random.shuffle(targets)
        self.assignedBuilding = targets[0]
        self.distance = self.assignedBuilding.location.distance

    def toWar(self):
        self.distance -= self.speed        

    def setToVillage(self):
        self.status = V_Status.TO_VILLAGE
        self.distance = self.assignedBuilding.location.distance

    def harvest(self):
        self.currentLoad[self.gatheringType] += self.producionSpeed
        self.assignedBuilding.currentResources -= self.producionSpeed

    def toLocation(self):
        self.distance -= self.speed
        if self.distance == 0:
            if self.assignedBuilding.buildTimeLeft <= 0:
                self.status = V_Status.HARVESTING
            else:
                self.status = V_Status.BUILDING

    def toVillage(self):
        self.distance -= self.speed
        if self.distance == 0:
            self.village.resources[self.gatheringType] += self.carryCapacity
            self.currentLoad[self.gatheringType] = 0
            self.status = V_Status.TO_LOCATION
            self.distance = self.assignedBuilding.location.distance

    def search(self):
        self.distance += 1
        if self.distance >= 9:
            return True
        return False
            # TODO make more complicated
    

if __name__ == '__main__':    
    from pprint import pprint
    for vType, villagerSettings in Defaults.simulation["villagers"].items():
        v = VillagerClass(vType, villagerSettings)
        pprint(v.__dict__)
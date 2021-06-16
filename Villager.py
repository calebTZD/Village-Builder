from Defaults import Defaults
from util import V_Status
import random

class VillagerClass:
    def __init__(self, vType, villagerSettings):
        self.type = vType

        #Defaults
        self.enhancemntFactor = Defaults.villagersConfig[self.type]["enhancemntFactor"]
        self.preferredBuilding = Defaults.villagersConfig[self.type]["preferredBuilding"]
        self.gatheringType = Defaults.villagersConfig[self.type]["gatheringType"]


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
        self.currentLoad = {
            "Food": 0,
            "Stone": 0,
            "Wood": 0,
            "Ore": 0,
            "Gold": 0,
            "ProjectX": 0,
            "Research": 0,
            }
        self.distance = 0
        self.assignedBuilding = None

        #Stats
        self.stats = {}

    def modify(self, base):
        return self.village.levelMod[self.type] * base

    def findBuilding(self):
        for building in self.village.buildings:
            if building.type == self.preferredBuilding:
                if len(building.villagers) < building.villagersAbleToSupport:
                    building.assignVillager(self)
                    self.distance = building.location.distance
                    return True
        return False      

    def build(self, building):
        self.village.build(self.preferredBuilding)
        # add building to village
        location = self.village.findLocationForBuilding(self.preferredBuilding)
        self.village.addBuilding(building, location)
        self.assignedBuilding = building

    def attacked(self, villager):
        self.currentHealth -= villager.modify(villager.attack)
        villager.currentHealth -= self.modify(self.defense)
        self.status = V_Status.DEAD
        if self.currentHealth <= 0:
            self.village.dead.append(self)
            self.village.villagers.pop(self)

    def attacking(self):
        if len(self.assignedBuilding.villagers) > 0:
            target = self.assignedBuilding.villagers[0]
            target.attacked(self)
        else:
            self.assignedBuilding.attacked(self)
            
    def findTarget(self):
        target = self.village.enemyVilages[0]
        targets = list(target.buildings)
        random.shuffle(targets)
        self.assignedBuilding = targets[0]        
        self.distance = self.assignedBuilding.location.distance

    def toWar(self):
        self.distance -= self.modify(self.speed)  
        if self.distance <= 0:
            self.assignedBuilding.enemies.append(self)

            
    def defending(self):
        if self.distance <= 0:
            if len(self.assignedBuilding.enemies) > 0:
                target = self.assignedBuilding.enemies[0]
                target.attacked(self)
            elif self.underAttack():
                building = self.underAttack()
                self.assignedBuilding = building
                self.distance = building.location.distance
            else:
                for building in self.village.buildings:
                    if building.type == "Barracks":
                        self.assignedBuilding = building
                        return
        else:
            self.distance -= self.modify(self.speed) 

    def setToVillage(self):
        self.status = V_Status.TO_VILLAGE
        self.distance = self.assignedBuilding.location.distance

    def harvest(self):
        self.currentLoad[self.gatheringType] += self.modify(self.productionSpeed)
        self.assignedBuilding.currentResources -= self.modify(self.productionSpeed)

    def toLocation(self):
        self.distance -= self.modify(self.speed) 
        if self.distance <= 0:
            if self.assignedBuilding.buildTimeLeft <= 0:
                if self.type == "Guard" or self.type == "Warrior":
                    self.status = V_Status.DEFENDING
                else:
                    self.status = V_Status.HARVESTING
            else:
                self.status = V_Status.BUILDING

    def toVillage(self):
        self.distance -= self.modify(self.speed) 
        if self.distance <= 0:
            self.village.resources[self.gatheringType] += self.modify(self.carryCapacity)
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
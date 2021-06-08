from Defaults import Defaults
from util import V_Status

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
        #TODO: Need to check to make sure we have enough space and if it is the closest building, etc.
        for building in self.village.buildings:
            if building.type == self.preferredBuilding:
                building.assignVillager(self)

if __name__ == '__main__':    
    from pprint import pprint
    for vType, villagerSettings in Defaults.simulation["villagers"].items():
        v = VillagerClass(vType, villagerSettings)
        pprint(v.__dict__)
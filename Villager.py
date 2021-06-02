from Defaults import Defaults

class Villager:
    def __init__(self, type):
        self.enhancemntFactor = Defaults.villagers[type]["enhancemntFactor"]
        self.speed = Defaults.simulation["villagers"][type]["speed"]
        self.maxHealth = Defaults.simulation["villagers"][type]["maxHealth"]
        self.carryCapacity = Defaults.simulation["villagers"][type]["carryCapacity"]
        self.attack = Defaults.simulation["villagers"][type]["attack"]
        self.defense = Defaults.simulation["villagers"][type]["defense"]
        self.productionSpeed = Defaults.simulation["villagers"][type]["productionSpeed"]
        self.spawnTime = Defaults.simulation["villagers"][type]["spawnTime"]
        self.enhancemntCost = Defaults.simulation["villagers"][type]["enhancemntCost"]
        self.spawnCost = Defaults.simulation["villagers"][type]["spawnCost"]
        self.currentHealth = int(self.maxHealth)
        self.currentLoad = {"": 0}
        self.status = "waiting"

from Defaults import Defaults

class BuildingClass:
    def __init__(self, bType, buildingSettings):
        self.type = bType

        #Defaults
        self.cost = Defaults.buildingsConfig[self.type]["cost"]
        self.villagersAbleToSupport = Defaults.buildingsConfig[self.type]["villagersAbleToSupport"]
        self.resource = Defaults.buildingsConfig[self.type]["resource"]
        self.enhancemntFactor = Defaults.buildingsConfig[self.type]["enhancemntFactor"]

        #Settings
        self.maxHealth = buildingSettings["maxHealth"]
        self.buildTime = buildingSettings["buildTime"]
        self.resourceAmount = buildingSettings["resourceAmount"]
        self.enhancemntCost = buildingSettings["enhancemntCost"]

        #Initial Values
        self.village = None
        self.location = None
        self.currentHealth = int(self.maxHealth)
        self.buildTimeLeft = self.buildTime
        self.currentResources = int(self.resourceAmount)
        self.villagers = []
        self.enemies = []

        #Stats
        self.stats = {}

    def assignVillager(self, villager):
        self.villagers.append(villager)
        villager.assignedBuilding = self

    def enemyPresent(self):
        if len(self.enemies) > 0:
            return True
        return False


if __name__ == '__main__':    
    from pprint import pprint
    from Location import LocationClass
    location = LocationClass('Grassland', Defaults.simulation["locations"]["Grassland"])    
    for bType, buildingSettings in Defaults.simulation["buildings"].items():
        b = BuildingClass(bType, buildingSettings)
        location.addBuilding(b)
        pprint(b.__dict__)
        pprint(b.location.__dict__)
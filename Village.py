from Defaults import Defaults

class VillageClass:
    def __init__(self, settings):
        #Defaults
        self.startingLocations = Defaults.villagesConfig["startingLocations"]
        self.startingBuildings = Defaults.villagesConfig["startingBuildings"]

        #Settings
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

        #Initial Values
        self.locations = []
        self.buildings = []
        self.villagers = []
        self.enemies = []

        #Stats
        self.stats = {}

    def addVillager(self, villager):
        self.villagers.append(villager)
        villager.village = self

    def addBuilding(self, building, location):
        location.addBuilding(building)
        self.buildings.append(building)
        building.village = self

    def addLocation(self, location):
        self.locations.append(location)
        location.village = self
    
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

    def build(self, type):
        # take resources away from village
        cost = Defaults.buildingsConfig[type]["cost"]
        for resource in cost:
            for reso in self.resources:
                if resource == reso:
                    self.resources[reso] -= cost[resource]

    def addEnemy(self, village):
        present = False
        for enemy in self.enemies:
            if enemy == village:
                present = True
        if not present:
            self.enemies.append(village)

if __name__ == '__main__':    
    from pprint import pprint 
    from Villager import VillagerClass       
    for villageSettings in Defaults.simulation["villages"]:
        village = VillageClass(villageSettings)

        for vType, villagerSettings in Defaults.simulation["villagers"].items():
            v = VillagerClass(vType, villagerSettings)
            village.addVillager(v)

        pprint(village.__dict__)
    
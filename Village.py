from Defaults import Defaults

class VillageClass:
    def __init__(self, settings):
        #Defaults

        #Settings
        self.name = settings["name"]
        self.priorities = settings["priorities"]
        #TODO Add resources to default data and UI
        self.resources = {
            "food": 0,
            "wood": 0,
            "stone": 0,
            "iron": 0,
            "gold": 0,
            "research": 0
        }

        #Initial Values
        self.locations = []
        self.buildings = []
        self.villagers = []

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

if __name__ == '__main__':    
    from pprint import pprint 
    from Villager import VillagerClass       
    for villageSettings in Defaults.simulation["villages"]:
        village = VillageClass(villageSettings)

        for vType, villagerSettings in Defaults.simulation["villagers"].items():
            v = VillagerClass(vType, villagerSettings)
            village.addVillager(v)

        pprint(village.__dict__)
    
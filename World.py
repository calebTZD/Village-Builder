from Defaults import Defaults

class WorldClass:
    def __init__(self, worldSettings):
        #Defaults
        
        #Settings
        self.days = worldSettings["days"]
        self.statValues = worldSettings["statValues"]
        self.numVillages = worldSettings["numVillages"]
        self.maxVillagersPerVillage = worldSettings["maxVillagersPerVillage"]
        self.startingVillagers = worldSettings["startingVillagers"]
        self.maxBuildingsPerVillage = worldSettings["maxBuildingsPerVillage"]

        #Initial Values
        self.villages = []

        #Stats
        self.stats = {}

    def addVillage(self, village):
        self.villages.append(village)

if __name__ == '__main__':    
    from pprint import pprint 
    from Village import VillageClass
    world = WorldClass(Defaults.simulation["world"])
    for villageSettings in Defaults.simulation["villages"]:
        village = VillageClass(villageSettings)
        world.addVillage(village)
    pprint(world.__dict__)
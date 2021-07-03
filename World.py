from Defaults import Defaults
from Stats import WorldStatsClass

class WorldClass:
    def __init__(self, sim, worldSettings):
        self.sim = sim
        self.initSettings(worldSettings)

        #Initial Values
        self.villages = []

        #Stats
        self.stats = WorldStatsClass(self)

    def toDict(self):
        return self.stats.statDict()

    def initSettings(self, worldSettings):
        self.days = int(worldSettings["days"])
        self.statValues = worldSettings["statValues"]
        self.numVillages = int(worldSettings["numVillages"])
        self.maxVillagersPerVillage = int(worldSettings["maxVillagersPerVillage"])
        self.startingVillagers = worldSettings["startingVillagers"]
        self.maxBuildingsPerVillage = int(worldSettings["maxBuildingsPerVillage"])   

    def addVillage(self, village):
        self.villages.append(village)
from Defaults import Defaults
from Stats import LocationStatsClass

class LocationClass:
    def __init__(self, lType, locationSettings):
        self.type = lType
        self.initSettings(locationSettings)     

        #Initial Values
        self.village = None
        self.buildings = []
        self.distance = self.calcDistance()

        #Stats
        self.stats = LocationStatsClass(self)

    def toDict(self):
        return self.stats.statDict()

    def initSettings(self, locationSettings):
        self.maxBuildings = int(locationSettings["maxBuildings"])
        self.buildingTypes = locationSettings["buildingTypes"]
        self.enhancemntFactor = int(locationSettings["enhancemntFactor"])
        self.numPerVillage = int(locationSettings["numPerVillage"])
        self.aveDistance = int(locationSettings["aveDistance"])
        self.enhancemntCost = int(locationSettings["enhancemntCost"]) 

    def calcDistance(self):
        #TODO: Need to finish this
        return self.aveDistance
    
    def addBuilding(self, building):
        #TODO: Need to validate building type and max buildings, etc.
        self.buildings.append(building)
        building.location = self
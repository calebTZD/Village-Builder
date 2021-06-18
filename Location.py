from Defaults import Defaults

class LocationClass:
    def __init__(self, lType, locationSettings):
        self.type = lType
        self.initSettings(locationSettings)     

        #Initial Values
        self.village = None
        self.buildings = []
        self.distance = self.calcDistance()

        #Stats
        self.stats = {}

    def initSettings(self, locationSettings):
        self.maxBuildings = locationSettings["maxBuildings"]
        self.buildingTypes = locationSettings["buildingTypes"]
        self.enhancemntFactor = locationSettings["enhancemntFactor"]
        self.numPerVillage = locationSettings["numPerVillage"]
        self.aveDistance = locationSettings["aveDistance"]
        self.enhancemntCost = locationSettings["enhancemntCost"]   

    def calcDistance(self):
        #TODO: Need to finish this
        return self.aveDistance
    
    def addBuilding(self, building):
        #TODO: Need to validate building type and max buildings, etc.
        self.buildings.append(building)
        building.location = self

if __name__ == '__main__':    
    from pprint import pprint
    for lType, locationSettings in Defaults.simulation["locations"].items():
        l = LocationClass(lType, locationSettings)
        pprint(l.__dict__)

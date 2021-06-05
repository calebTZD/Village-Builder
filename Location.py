from Defaults import Defaults

class LocationClass:
    def __init__(self, lType, locationSettings):
        self.type = lType

        #Defaults
        self.maxBuildings = Defaults.locationsConfig[self.type]["maxBuildings"]
        self.buildingTypes = Defaults.locationsConfig[self.type]["buildingTypes"]
        self.enhancemntFactor = Defaults.locationsConfig[self.type]["enhancemntFactor"]

        #Settings
        self.numPerVillage = locationSettings["numPerVillage"]
        self.aveDistance = locationSettings["aveDistance"]
        self.enhancemntCost = locationSettings["enhancemntCost"]

        #Initial Values
        self.village = None
        self.buildings = []

        #Stats
        self.stats = {}
    
    def addBuilding(self, building):
        #TODO: Need to validate building type and max buildings, etc.
        self.buildings.append(building)
        building.location = self

if __name__ == '__main__':    
    from pprint import pprint
    for lType, locationSettings in Defaults.simulation["locations"].items():
        l = LocationClass(lType, locationSettings)
        pprint(l.__dict__)

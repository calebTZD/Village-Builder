from Defaults import Defaults

class Location:
    def __init__(self, type):
        self.maxBuildings = Defaults.locations[type]["maxBuildings"]
        self.buildingTypes = Defaults.locations[type]["buildingTypes"]
        self.enhancemntFactor = Defaults.locations[type]["enhancemntFactor"]
        self.numPerVillage = Defaults.simulation["locations"][type]["numPerVillage"]
        self.aveDistance = Defaults.simulation["locations"][type]["aveDistance"]
        self.enhancemntCost = Defaults.simulation["locations"][type]["enhancemntCost"]
        self.currentBuildings = 0

from Defaults import Defaults

class Building:
    def __init__(self, type):
        self.cost = Defaults.buildings[type]["cost"]
        self.villagersAbleToSupport = Defaults.buildings[type]["villagersAbleToSupport"]
        self.resource = Defaults.buildings[type]["resource"]
        self.enhancemntFactor = Defaults.buildings[type]["enhancemntFactor"]
        self.maxHealth = Defaults.simulation["buildings"][type]["maxHealth"]
        self.buildTime = Defaults.simulation["buildings"][type]["buildTime"]
        self.resourceAmount = Defaults.simulation["buildings"][type]["resourceAmount"]
        self.enhancemntCost = Defaults.simulation["buildings"][type]["enhancemntCost"]
        self.currentHealth = int(self.maxHealth)
        self.currentResources = int(self.resourceAmount)
        self.villagers = 0


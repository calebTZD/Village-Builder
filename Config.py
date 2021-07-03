from copy import copy
from Defaults import Defaults


class ConfigClass:
    def __init__(self, simulation):
        self.world = dict(Defaults.worldConfig)
        self.villages = {}
        self.villagers = dict(Defaults.villagersConfig)
        self.locations = dict(Defaults.locationsConfig)
        self.buildings = dict(Defaults.buildingsConfig)

        self.initWorld(simulation)
        self.initVillages(simulation)
        self.initVillagers(simulation)
        self.initLocations(simulation)
        self.initBuildings(simulation)

    def toDict(self):
        return {
            'world': self.world,
            'villages': self.villages,
            'villagers': self.villagers,
            'locations': self.locations,
            'buildings': self.buildings
        }

    def initWorld(self, simulation):        
        for setting in simulation['world']:
            self.world[setting] = copy(simulation['world'][setting])
 
    def initVillages(self, simulation):        
        for village in simulation['villages']:
            self.villages[village['name']] = dict(Defaults.villagesConfig)
            self.villages[village['name']].update(dict(village))

    def initVillagers(self, simulation):        
        for vType in simulation['villagers']:
            vTypeSettings = simulation['villagers'][vType]
            for setting in vTypeSettings:
                self.villagers[vType][setting] = copy(vTypeSettings[setting])                

    def initLocations(self, simulation):        
        for lType in simulation['locations']:
            lTypeSettings = simulation['locations'][lType]
            for setting in lTypeSettings:
                self.locations[lType][setting] = copy(lTypeSettings[setting])   

    def initBuildings(self, simulation):        
        for bType in simulation['buildings']:
            bTypeSettings = simulation['buildings'][bType]
            for setting in bTypeSettings:
                self.buildings[bType][setting] = copy(bTypeSettings[setting])
import json

class DefaultsClass:
    def __init__(self):
        self.simulation = self.initDefaultSimulation()
        self.villages = self.initDefaultVillages()
        self.simulation["villages"] = self.villages
        config = self.readConfig()
        self.villagers = config["villagers"]
        self.buildings = config["buildings"]
        self.locations = config["locations"]


    def initDefaultSimulation(self):
        f = open("iData.json","r")
        lines = f.readlines()
        f.close()
        sData = ""
        for line in lines:
            sData += line.rstrip()
        sim = json.loads(sData)
        return sim
    
    def initDefaultVillages(self):
        f = open("iDataVillages.json","r")
        lines = f.readlines()
        f.close()
        sData = ""
        for line in lines:
            sData += line.rstrip()
        villages = json.loads(sData)
        return villages

    def readConfig(self):
        f = open("iDataConfig.json" , "r")
        lines = f.readlines()
        f.close()
        sData = ""
        for line in lines:
            sData += line.rstrip()
        config = json.loads(sData)
        return config


Defaults = DefaultsClass()

if __name__ == '__main__':
    from pprint import pprint
    # pprint(Defaults.simulation)
    pprint(Defaults.villagers)
    pprint(Defaults.buildings)
    pprint(Defaults.locations)
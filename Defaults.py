import json

class DefaultsClass:
    def __init__(self):
        self.simulation = self.initDefaultSimulation()
        self.villages = self.initDefaultVillages()
        self.simulation["villages"] = self.villages
        config = self.readConfig()
        self.worldConfig = config["world"]
        self.villagesConfig = config["villages"]
        self.villagersConfig = config["villagers"]
        self.buildingsConfig = config["buildings"]
        self.locationsConfig = config["locations"]


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
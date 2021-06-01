import json

class DefaultsClass:
    def __init__(self):
        self.simulation = self.initDefaultSimulation()
        self.villages = self.initDefaultVillages()
        self.simulation["villages"] = self.villages

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

Defaults = DefaultsClass()

if __name__ == '__main__':
    from pprint import pprint
    pprint(Defaults.simulation)
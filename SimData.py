from warnings import simplefilter
from DB import DB

class SimDataClass:
    def __init__(self):
        self.db = DB

    def getAllSimNames(self):
        cursor = DB.SimCol.find({}, {"name": 1})
        simNames = []
        for sim in cursor:
            simNames.append(sim["name"])
        return simNames
    
    def getSymByName(self, name):
        sim = self.db.SimCol.find_one({'name': name})
        if sim:
            sim.pop('_id', None)
        return sim

    def createSym(self, simData):
        sim = self.db.SimCol.insert_one(simData) 
        if sim:
            return True
        else:
            return False

    def deleteSym(self, name):
        sim = self.db.SimCol.delete_one({"name": name})
        if sim:
            return True
        else:
            return False

    def getWorld(self, simName):
        sim = self.db.SimCol.find_one({'name': simName}, {"world": 1})
        if sim:
            return sim["world"]            

    def updateWorld(self, simName, wordData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"world": wordData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    def getVillages(self, simName):
        sim = self.db.SimCol.find_one({'name': simName}, {"villages": 1})
        if sim:
            return sim["villages"]

    def updateVillages(self, simName, villagesData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villages": villagesData}})
        if results and results.matched_count == 1:
            for v in villagesData:
                self.updateVillage(simName, v)
            return True
        else:
            return False


    def getVillagers(self, simName):
        sim = self.db.SimCol.find_one({'name': simName}, {"villagers": 1})
        if sim:
            return sim["villagers"]

    def updateVillagers(self, simName, villData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villagers": villData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    def getLocations(self, simName):
        sim = self.db.SimCol.find_one({'name': simName}, {"locations": 1})
        if sim:
            return sim["locations"]

    def updateLocations(self, simName, locationsData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"locations": locationsData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    def getBuildings(self, simName):
        sim = self.db.SimCol.find_one({'name': simName}, {"buildings": 1})
        if sim:
            return sim["buildings"]

    def updateBuildings(self, simName, buildingsData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"buildings": buildingsData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    def getAllVillages(self):
        return list(DB.VillageCol.find())

    def updateVillage(self, simulationName, villageData):
        villageData['simulationName'] = simulationName
        results =  DB.VillageCol.replace_one({"name": villageData['name'], "simulationName": simulationName}, villageData, upsert=True)



SimData = SimDataClass()

if __name__ == '__main__':
    from pprint import pprint
    import json

    # simNames = SimData.getAllSimNames()
    # pprint(simNames)
    # sim = SimData.getSymByName("The Myst2")
    # pprint(sim)
    # world = SimData.getWorld("The Myst")
    # pprint(world)
    # world["days"] = 55
    # resulst = SimData.updateWorld("The Myst", world)
    # pprint(resulst)
    # world = SimData.getWorld("The Myst")
    # pprint(world)

    # SimData.createSym({"name": "Boldune"})
    # sim = SimData.getSymByName("Boldune")
    # pprint(sim)

    # SimData.deleteSym("The Myst")
    # world = SimData.getSymByName"The Myst")
    # pprint(world)

    # vill = SimData.getVillages("The Myst")
    # pprint(vill)
    # vill[0] = 55
    # resulst = SimData.updateVillages("The Myst", vill)
    # pprint(resulst)
    # vill = SimData.getVillages("The Myst")
    # pprint(vill)

    # gers = SimData.getVillagers("The Myst")
    # pprint(gers)
    # gers["Farmer"]["speed"] = 55
    # resulst = SimData.updateVillagers("The Myst", gers)
    # pprint(resulst)
    # gers = SimData.getVillagers("The Myst")
    # pprint(gers)

    # loc = SimData.getLocations("The Myst")
    # pprint(loc)
    # loc["Grassland"]["numPerVillage"] = 55
    # resulst = SimData.updateLocations("The Myst", loc)
    # pprint(resulst)
    # loc = SimData.getLocations("The Myst")
    # pprint(loc)

    # bul = SimData.getBuildings("The Myst")
    # pprint(bul)
    # bul["LoggingCamp"]["maxHealth"] = 55
    # resulst = SimData.updateBuildings("The Myst", bul)
    # pprint(resulst)
    # bul = SimData.getBuildings("The Myst")
    # pprint(bul)

#########################################################   
# Villages
#########################################################
    # villages = SimData.getAllVillages()
    # pprint(len(villages))
    # v = villages[0]
    # v.pop('_id', None)
    # SimData.updateVillage("test", v)
    # villages = SimData.getAllVillages()
    # pprint(len(villages))
    # v["priorities"]["FoodProduction"] = 77
    # SimData.updateVillage("test", v)
    # villages = SimData.getAllVillages()
    # pprint(villages)

    # vill = SimData.getVillages("The Myst")
    # SimData.updateVillages("The Myst", vill)
    # villages = SimData.getAllVillages()
    # pprint(villages)
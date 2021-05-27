from DB import DB

class SimDataClass:
    def __init__(self):
        self.db = DB

    def getByName(self, name):
        return self.db.SimCol.find_one({'name': name})

    def create(self, simData):
        sim = self.db.SimCol.insert_one(simData) 
        if sim:
            return True
        else:
            return False

    def delete(self, name):
        sim = self.db.SimCol.delete_one({"name": name})
        if sim:
            return True
        else:
            return False

    def getWorld(self, simName):
        sim = self.db.SimCol.find_one({'name': simName})
        if sim:
            return sim["world"]            

    def updateWorld(self, simName, wordData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"world": wordData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    def updateVillages(self, simName, villagesData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villages": villagesData}})
        if results and results.matched_count == 1:
            for v in villagesData:
                self.updateVillage(simName, v)
            return True
        else:
            return False

    def updateVillagers(self, simName, villData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villagers": villData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False


    def updateLocations(self, simName, locationsData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villagers": locationsData}})
        if results and results.matched_count == 1:
            return True
        else:
            return False

    
    def updateBuildings(self, simName, buildingsData):
        results =  DB.SimCol.update_one({"name": simName}, {"$set": {"villagers": buildingsData}})
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
    # world = SimData.getWorld("The Myst")
    # pprint(world)
    # world["settings"]["days"] = 55
    # resulst = SimData.updateWorld("The Myst", world)
    # pprint(resulst)
    # world = SimData.getWorld("The Myst")
    # pprint(SimData.delete("The Myst"))

#########################################################   
# Villages
#########################################################
    villages = SimData.getAllVillages()
    pprint(len(villages))
    v = villages[0]
    v.pop('_id', None)
    SimData.updateVillage("test", v)
    villages = SimData.getAllVillages()
    pprint(len(villages))
    v["priorities"]["FoodProduction"] = 77
    SimData.updateVillage("test", v)
    villages = SimData.getAllVillages()
    pprint(villages)

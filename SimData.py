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
    
    def getSimByName(self, name):
        sim = self.db.SimCol.find_one({'name': name})
        if sim:
            sim.pop('_id', None)
        return sim

    def createSim(self, simData):
        sim = self.db.SimCol.insert_one(simData) 
        if sim:
            return True
        else:
            return False

    def deleteSim(self, name):
        sim = self.db.SimCol.delete_one({"name": name})
        if sim:
            return True
        else:
            return False

    def getSimStatus(self, name):
        sim = self.db.SimCol.find_one({'name': name}, {"status": 1})
        if sim:
            return sim["status"]

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
        cursor = DB.VillageCol.find()
        villages = []
        for village in cursor:
            village.pop('_id', None)
            villages.append(village)
        return villages

    def updateVillage(self, simulationName, villageData):
        villageData['simulationName'] = simulationName
        results =  DB.VillageCol.replace_one({"name": villageData['name'], "simulationName": simulationName}, villageData, upsert=True)

    def getStatsByName(self, simName):
        cursor = self.db.StatsCol.find({'simName': simName}, {'simName': 1, 'timeStamp': 1})
        stats = []
        for item in cursor:
            item.pop('_id', None)
            stats.append(item)
        return stats

    def getStatsByRun(self, simName, timeStamp):
        stats = self.db.StatsCol.find_one({'simName': simName, 'timeStamp': timeStamp})
        if stats:
            stats.pop('_id', None)
        return stats

    def saveStats(self, statsData):
        results =  DB.StatsCol.insert_one(statsData)

    def deleteStats(self, name):
        sim = self.db.StatsCol.delete_one({"simName": name})
        if sim:
            return True
        else:
            return False

SimData = SimDataClass()

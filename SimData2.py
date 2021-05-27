from DB import DB

class SimDataClass:
    def __init__(self):
        self.db = DB

    def getSimByName(self, name):
        return self.db.SimCol.find_one({'name': name})

    def createSim(self, simData):
        pass
        #self.db.initalValCol.replace_one({"vId": valData["vId"]}, valData, upsert=True) 

    def deleteSim(self):
        pass
        #return self.db.initalValCol.find_one()
    
    def getWorld(self, simName):
        sim = self.db.SimCol.find_one({'name': simName})
        if sim:
            return sim["world"]            

    def updateWorld(self, simName, wordData):
        return DB.SimCol.update_one({"name": simName}, {"$set": {"world": wordData}})

    def updateSimVillages(self, name, villagesData):
        pass

    def updateSimVillagers(self, name, villagersData):
        pass

    def updateSimLocations(self, name, locationsData):
        pass
    
    def updateSimBuildings(self, name, buildingsData):
        pass




SimData = SimDataClass()

if __name__ == '__main__':
    from pprint import pprint
    import json
    world = SimData.getWorld("The Myst")
    pprint(world)
    world["settings"]["days"] = 55
    resulst = SimData.updateWorld("The Myst", world)
    pprint(resulst)
    world = SimData.getWorld("The Myst")
    pprint(world)


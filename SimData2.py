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
    
    def updateSimWorld(self, name, wordData):
        pass

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
    sim = SimData.getSimByName("The Myst")
    pprint(sim)


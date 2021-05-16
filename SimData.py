from DB import DB

class villageDataClass:
    def __init__(self):
        self.db = VillageDB

    def getInitalVals(self, villageid):
        return self.db.initalValCol.find_one({'vId': villageid})

    def storeVals(self, valData):
        self.db.initalValCol.replace_one({"vId": valData["vId"]}, valData, upsert=True) 

    def getInitalResources(self):
        return self.db.initalValCol.find_one()

villageData = villageDataClass()

if __name__== "__main__":
    from initDB import *
    from pprint import pprint
    villageData.db.initGamesCollection()
    villageData.storeVals(inVals)
    pprint(villageData.getInitalResources())
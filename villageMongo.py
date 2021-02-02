from DB import VillageDB

class villageData:
    def __init__(self):
        self.db = VillageDB

    def getInitalVals(self, villageid):
        return self.db.initalValCol.find_one({'initalValCol': villageid})

    def storeVals(self, valData):
        self.db.initalValCol.replace_one({"initalValCol": valData["initalValCol"]}, valData, upsert=True) 

Data = villageData()

if __name__== "__main__":
    from initDB import *
    Data.db.initGamesCollection()
    Data.storeVals(inVals)
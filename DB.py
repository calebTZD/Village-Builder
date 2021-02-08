from pymongo import MongoClient

class villageData:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/admin")
        self.villageDB = self.client["villageBuilder"]
        self.initalValCol = self.villageDB["initalValues"]

    def initGamesCollection(self):
        initalValCol = self.villageDB["villageBuilder"]
        initalValCol.drop()
        initalValCol.create_index('VillageId')
        


VillageDB = villageData()

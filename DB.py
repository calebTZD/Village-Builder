from pymongo import MongoClient

class DBaccess:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/admin")
        self.villageDB = self.client["RTSDB"]
        self.SimCol = self.villageDB["Sims"]
        self.VillageCol = self.villageDB["Villages"]
        self.StatCol = self.villageDB["Stats"]

    def initSimCollection(self):
        self.SimCol.drop()
        self.SimCol.create_index("name", unique=True)
        


DB = DBaccess()

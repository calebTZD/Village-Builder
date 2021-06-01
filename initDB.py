from DB import DB
from Defaults import Defaults
from pprint import pprint
import json

def initSimulationsCollection():
    DB.initSimCollection()
    


#################################################################
# Villages
################################################################
def initVillagesCollection():
    DB.initVillagesCollection()
    f = open("iDataVillages.json","r")
    lines = f.readlines()
    sData = ""
    for line in lines:
        sData += line.rstrip()
    villages = json.loads(sData)
    for v in villages:
        v['simulationName'] = "Default"
        DB.VillageCol.insert_one(v)


def addSampleData():
    #Simulation
    results = DB.SimCol.insert_one(Defaults.simulation)
    #Villages
    # for v in Defaults.villages:
    #     v['simulationName'] = "Default"
    #     DB.VillageCol.insert_one(v)


if __name__ == '__main__':
    initSimulationsCollection()
    initVillagesCollection()
    addSampleData()
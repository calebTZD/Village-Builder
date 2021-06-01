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

def addSampleData():
    #Simulation
    sampleSim = dict(Defaults.simulation)
    sampleSim["name"] = "The Myst"
    results = DB.SimCol.insert_one(sampleSim)

    #Villages
    for v in Defaults.villages:
        village = dict(v)
        village['simulationName'] = "The Myst"
        DB.VillageCol.insert_one(v)


if __name__ == '__main__':
    initSimulationsCollection()
    initVillagesCollection()
    addSampleData()
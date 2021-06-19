from DB import DB
from Defaults import Defaults
from pprint import pprint
import json

def initSimulationsCollection():
    DB.initSimCollection()

def initVillagesCollection():
    DB.initVillagesCollection()

def initStatsCollection():
    DB.initStatsCollection()

def addSampleData():
    #Simulation
    sampleSim = dict(Defaults.simulation)
    sampleSim["name"] = "The Myst"
    results = DB.SimCol.insert_one(sampleSim)

    #Villages
    for v in Defaults.villages:
        village = dict(v)
        village['simulationName'] = "The Myst"
        DB.VillageCol.insert_one(village)

if __name__ == '__main__':
    initSimulationsCollection()
    initVillagesCollection()
    initStatsCollection()
    addSampleData()
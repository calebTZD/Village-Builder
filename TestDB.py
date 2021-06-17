from pprint import pprint
import json
from SimData import SimData
import initDB

#########################################################   
# Villages
#########################################################
def testSimulations():
    simNames = SimData.getAllSimNames()
    pprint(simNames)
    sim = SimData.getSymByName("The Myst")
    pprint(sim)
    world = SimData.getWorld("The Myst")
    pprint(world)
    world["days"] = 55
    resulst = SimData.updateWorld("The Myst", world)
    pprint(resulst)
    world = SimData.getWorld("The Myst")
    pprint(world)

    SimData.createSym({"name": "Boldune"})
    sim = SimData.getSymByName("Boldune")
    pprint(sim)

    # SimData.deleteSym("The Myst")
    # world = SimData.getSymByName("The Myst")
    # pprint(world)

def testSymVillages():
    vill = SimData.getVillages("The Myst")
    pprint(vill)
    vill[0]["priorities"]["Food"] = 55
    results = SimData.updateVillages("The Myst", vill)
    pprint(results)
    vill = SimData.getVillages("The Myst")
    pprint(vill)

def testSymVillagers():
    gers = SimData.getVillagers("The Myst")
    pprint(gers)
    gers["Farmer"]["speed"] = 55
    resulst = SimData.updateVillagers("The Myst", gers)
    pprint(resulst)
    gers = SimData.getVillagers("The Myst")
    pprint(gers)

def testSymLocations():
    loc = SimData.getLocations("The Myst")
    pprint(loc)
    loc["Grassland"]["numPerVillage"] = 55
    resulst = SimData.updateLocations("The Myst", loc)
    pprint(resulst)
    loc = SimData.getLocations("The Myst")
    pprint(loc)

def testSymBuildings():
    bul = SimData.getBuildings("The Myst")
    pprint(bul)
    bul["LoggingCamp"]["maxHealth"] = 55
    resulst = SimData.updateBuildings("The Myst", bul)
    pprint(resulst)
    bul = SimData.getBuildings("The Myst")
    pprint(bul)


#########################################################   
# Villages
#########################################################
def testVillages():
    villages = SimData.getAllVillages()
    pprint(len(villages))
    v = villages[0]
    v.pop('_id', None)
    SimData.updateVillage("test", v)
    villages = SimData.getAllVillages()
    pprint(len(villages))
    v["priorities"]["Food"] = 77
    SimData.updateVillage("test", v)
    villages = SimData.getAllVillages()
    pprint(villages)

    vill = SimData.getVillages("The Myst")
    SimData.updateVillages("The Myst", vill)
    villages = SimData.getAllVillages()
    pprint(villages)

def testStats():
    SimData.saveStats({'simName': "testy", 'value': 1})
    testy = SimData.getStatsByName("testy")
    pprint(testy)
    SimData.deleteStats("testy")
    testy = SimData.getStatsByName("testy")
    pprint(testy)

if __name__ == '__main__':
    initDB.initSimulationsCollection()
    initDB.initVillagesCollection()
    initDB.initStatsCollection()
    initDB.addSampleData()
    # testSimulations()
    # testSymVillages()
    # testSymVillagers()
    # testSymLocations()
    # testSymBuildings()
    # testVillages()
    testStats()

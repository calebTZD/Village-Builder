from DB import DB
from pprint import pprint
import json


#################################################################
# Simulations
################################################################
DB.initSimCollection()
f = open("iData.json","r")
lines = f.readlines()
sData = ""
for line in lines:
    sData += line.rstrip()
obj = json.loads(sData)
results = DB.SimCol.insert_one(obj)
data = DB.SimCol.find_one()
pprint(data)


#################################################################
# Villages
################################################################
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
data = list(DB.VillageCol.find())
pprint(len(data))

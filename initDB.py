from DB import DB
from pprint import pprint
import json

DB.initSimCollection()
data = DB.SimCol.find_one()
pprint(data)

f = open("iData.json","r")
lines = f.readlines()
sData = ""
for line in lines:
    sData += line.rstrip()
obj = json.loads(sData)
results = DB.SimCol.replace_one({"name": obj["name"]}, obj, upsert=True)
#results.modified_count = 1 if update otherwise created
data = DB.SimCol.find_one()
pprint(data["name"])

#UPDATE
wObj = obj["world"]
wObj["days"] = 50
results = DB.SimCol.update_one({"name": obj["name"]}, {"$set": {"world": wObj}})
pprint(results.modified_count) #If 0 update did not happen
data = DB.SimCol.find_one({'name': obj["name"]})
pprint(data["world"])
pprint(data)

#DELETE
# results = DB.SimCol.delete_one({"name": obj["name"]})
# pprint(results.deleted_count) #If 0 update did not happen
# data = DB.SimCol.find_one({'name': obj["name"]})
# pprint(data["name"])

# obj["name"] = "Riven"
# DB.SimCol.replace_one({"name": obj["name"]}, obj, upsert=True)
# data = DB.SimCol.find_one({'name': "Riven"})
# pprint(data["name"])



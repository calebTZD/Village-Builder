from flask import Flask, request, make_response, render_template, redirect, url_for, after_this_request, jsonify
from flask_socketio import SocketIO
import traceback, json
from bson import json_util


from villageMongo import villageData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' #TODO: Change this
app.config["CACHE_TYPE"] = "null"

def serializeToJSON(data):
    data.pop('_id', None)
    return json.dumps(data)

##############################################################################
#                        WebSockets
##############################################################################

gamesocket = SocketIO(app)

##############################################################################
#                        REST API
##############################################################################

@app.route('/') #root redirect
def index():
    return redirect(url_for('static', filename='Simulation.html'))

@app.route('/getData')
def getResource():
    #data = villageData.getInitalResources() #TODO: remove hardcoded data
    f = open("iData.json","r")
    lines = f.readlines()
    sData = ""
    for line in lines:
        sData += line.rstrip()
    data = json.loads(sData)
    return serializeToJSON(data)

@app.route('/getVillages')
def getVillages():
    #data = villageData.getInitalResources() #TODO: remove hardcoded data
    f = open("iDataVillages.json","r")
    lines = f.readlines()
    sData = ""
    for line in lines:
        sData += line.rstrip()
    data = json.loads(sData)
    villages = {}
    for village in data:
        villages[village['fixed']['name']] = village
    return json.dumps(villages)

class InvalidUsageExeption(Exception):
    def __init__(self, message, status_code=400, data={}):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        result = dict(self.data or ())
        result['message'] = self.message
        return result

@app.errorhandler(InvalidUsageExeption)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



if __name__ == '__main__':
    gamesocket.run(app)
    
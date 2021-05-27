from flask import Flask, request, make_response, render_template, redirect, url_for, after_this_request, jsonify
from flask_socketio import SocketIO
import sys, traceback, json
from bson import json_util

from SimData import SimData

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

@app.route('/updateVillages', methods = ['POST'])
def updateVillages():
    try:
        simName = request.args.get('simName')
        villages = json.loads(request.data)
        results = SimData.updateVillages(simName, villages)
        if results == True:
            return "Success"
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update Villages.", status_code=400)

@app.route('/getVillages', methods = ['GET'])
def getVillages():
    try:
        simName = request.args.get('simName')
        villages = SimData.getVillages(simName)
        return json.dumps(villages)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to get Villages.", status_code=400)
    

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
    
from flask import Flask, request, make_response, render_template, redirect, url_for, after_this_request, jsonify
from flask_socketio import SocketIO
import sys, traceback, json
from bson import json_util

from SimData import SimData

from Defaults import Defaults

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
#                       REST API
##############################################################################

@app.route('/') #root redirect
def index():
    return redirect(url_for('static', filename='Simulation.html'))

@app.route('/getSims', methods = ['GET'])
def getSims():
    try:
        sims = SimData.getAllSimNames()
        if not sims:
                raise NameError("Simulations not found")
        return json.dumps(sims)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load simulation.", status_code=400)

@app.route('/getSim', methods = ['GET'])
def getSim():
    try:
        simName = request.args.get('simName')
        sim = SimData.getSimByName(simName)
        if not sim:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(sim)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update simulation.", status_code=400)

@app.route('/createSim', methods = ['GET'])
def createSim():
    try:
        simName = request.args.get('simName')
        newSim = dict(Defaults.simulation)
        newSim["name"] = simName
        SimData.createSim(newSim)
        sim = SimData.getSimByName(simName)
        if not sim:
                raise NameError("Simulation not created: " + simName)
        return json.dumps(sim)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to create simulation.", status_code=400)

@app.route('/deleteSim', methods = ['GET'])
def deleteSim():
    try:
        simName = request.args.get('simName')
        results = SimData.deleteSim(simName)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")    
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to delete simulation.", status_code=400)

@app.route('/getSimStatus', methods = ['GET'])
def getSimStatus():
    try:
        simName = request.args.get('simName')
        status = SimData.getSimStatus(simName)
        if not status:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(status)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load status.", status_code=400)

@app.route('/getWorld', methods = ['GET'])
def getWorld():
    try:
        simName = request.args.get('simName')
        world = SimData.getWorld(simName)
        if not world:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(world)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load World.", status_code=400)

@app.route('/updateWorld', methods = ['POST'])
def updateWorld():
    try:
        simName = request.args.get('simName')
        world = json.loads(request.data)
        results = SimData.updateWorld(simName, world)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update World.", status_code=400)

@app.route('/getVillages', methods = ['GET'])
def getVillages():
    try:
        simName = request.args.get('simName')
        villages = SimData.getVillages(simName)

        if not villages:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(villages)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update Villages.", status_code=400)

@app.route('/updateVillages', methods = ['POST'])
def updateVillages():
    try:
        simName = request.args.get('simName')
        villages = json.loads(request.data)
        results = SimData.updateVillages(simName, villages)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update Villages.", status_code=400)

@app.route('/getVillagers', methods = ['GET'])
def getVillagers():
    try:
        simName = request.args.get('simName')
        villagers = SimData.getVillagers(simName)
        if not villagers:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(villagers)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load Villagers.", status_code=400)

@app.route('/updateVillagers', methods = ['POST'])
def updateVillagers():
    try:
        simName = request.args.get('simName')
        villagers = json.loads(request.data)
        results = SimData.updateVillagers(simName, villagers)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update Villagers.", status_code=400)

@app.route('/getLocations', methods = ['GET'])
def getLocations():
    try:
        simName = request.args.get('simName')
        locations = SimData.getLocations(simName)
        if not locations:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(locations)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load locations.", status_code=400)

@app.route('/updateLocations', methods = ['POST'])
def updateLocations():
    try:
        simName = request.args.get('simName')
        locations = json.loads(request.data)
        results = SimData.updateLocations(simName, locations)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update locations.", status_code=400)

@app.route('/getBuildings', methods = ['GET'])
def getBuildings():
    try:
        simName = request.args.get('simName')
        buildings = SimData.getBuildings(simName)
        if not buildings:
                raise NameError("Simulation not found: " + simName)
        return json.dumps(buildings)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load buildings.", status_code=400)

@app.route('/updateBuildings', methods = ['POST'])
def updateBuildings():
    try:
        simName = request.args.get('simName')
        building = json.loads(request.data)
        results = SimData.updateBuildings(simName, building)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update buildings.", status_code=400)

@app.route('/getAllVillages')
def getAllVillages():
    try:
        villages = SimData.getAllVillages()
        if not villages:
                raise NameError("Villages not found")
        return json.dumps(villages)
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to load Villages.", status_code=400)

@app.route('/updateVillage', methods = ['POST'])
def updateVillage():
    try:
        simName = request.args.get('simName')
        vData = json.loads(request.data)
        results = SimData.updateVillage(simName, vData)
        if results == True:
            return json.dumps({'status': "Success"})
        else:
            raise Exception("Failure")
    except:
        traceback.print_exc(file=sys.stdout)
        raise InvalidUsageExeption("Failed to update Village.", status_code=400)


class InvalidUsageExeption(Exception):
    def __init__(self, message, status_code=400, data={}):
        Exception.__init__(self)
        self.error = message
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        result = dict(self.data or ())
        result['error'] = self.error
        return result

@app.errorhandler(InvalidUsageExeption)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



if __name__ == '__main__':
    gamesocket.run(app)
    
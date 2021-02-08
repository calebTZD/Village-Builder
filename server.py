from flask import Flask, request, make_response, render_template, redirect, url_for, after_this_request, jsonify
from flask_socketio import SocketIO
import traceback, json

from villageMongo import villageData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' #TODO: Change this
app.config["CACHE_TYPE"] = "null"

##############################################################################
#                        WebSockets
##############################################################################

gamesocket = SocketIO(app)

##############################################################################
#                        REST API
##############################################################################

@app.route('/') #root redirect
def index():
    return redirect(url_for('static', filename='Village.html'))

@app.route('/villager/workSpeed')
def workSpeed():
    vilager = request.args.get('vil')

    return '2'

@app.route('/getResource')
def getResource():
    resources = villageData.getInitalResources()
    return json.dumps(resources)

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
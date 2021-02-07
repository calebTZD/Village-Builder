from flask import Flask, request, make_response, render_template, redirect, url_for, after_this_request, jsonify
from flask_socketio import SocketIO
import traceback, json

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
    return redirect(url_for('static', filename='Add.html'))

@app.route('/add2')
def add2():
    x = request.args.get('x')
    y = request.args.get('y')
    resultObj = {
        'x': x,
        'y': y,
        'value': int(x)+int(y)
    }
    return json.dumps(resultObj)

@app.route('/addMany')
def addMany():
    numbers = json.loads(request.data)
    value = 0
    for number in numbers:
        value += number
    resultObj = {
        'numbers': numbers,
        'value': value
    }
    return json.dumps(resultObj)


@app.route('/getResourceTypes')
def getResourceTypes():
    resources = ['wood', 'grain', 'ore']
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
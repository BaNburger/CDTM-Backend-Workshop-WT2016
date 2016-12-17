from flask import Flask,render_template,send_file,jsonify
from list import List
from task import Task


defaultList = List(0, "defaultList")

List1 = List(1, "Revolver")
List2 = List(2, "Abbey Roads")
Lists = [defaultList, List1, List2]
ListDict = {}
#for LList in Lists:
#    ListDict[LList.id] = LList

Task1 = Task(1, "Penny Lane")
Task2 = Task(2, "Yellow Submarine")
Task3 = Task(3, "Octopuses Garden")
Task4 = Task(4, "Lady Madonna")
Tasks = [Task1, Task2, Task3, Task4]

# create a new server app
app = Flask(__name__, static_url_path="")

# define all accessible routes
@app.route('/', methods=['GET'])
def homepage():
    return send_file("static/index.html")
    #return render_template("index.html")

@app.route("/api/version", methods=["GET"])
def dostuff():
    return jsonify({ "_version":1 })

@app.route("/api/lists", methods=["GET"])
def domorestuff():
    return jsonify({ "_lists": [x.__dict__ for x in Lists] })

@app.route("/api/lists/<int:listId>/tasks", methods=["GET"])
def dosomestuff(listId):
    return jsonify({ "_tasks": [x.__dict__ for x in Tasks if x.list==listId]})

if __name__ == '__main__':
    addr = "localhost"         # the same as 127.0.0.1
    port = 1337
    debug = True               # activates the [1] debugger, [2] automatic reloader
    app.run(host=addr, port=port, debug=debug)

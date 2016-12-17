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
    return jsonify({ "_version":4.0 })

@app.route("/api/lists", methods=["GET"])
def domorestuff():
    return jsonify({ "_lists": [x.__dict__ for x in Lists] })

@app.route("/api/lists/<int:listId>/tasks", methods=["GET"])
def dosomestuff(listId):
    return jsonify({ "_tasks": [x.__dict__ for x in Tasks if x.list==listId]})

@app.route("/api/lists/<int:listId>/tasks", methods=["POST"])
def postsometask(listId):
#    newTask = task.Task(listId, request.get_json().__dict__["title"])
#    Tasks.append(newTask)
    ''' creates a new task for a list '''
    if (len([l for l in Lists if l.listId == listId]) < 1):
        json_abort(404, 'List not found')
    try:
         data = request.get_json()
    except:
        json_abort(400, 'No JSON provided')

    if data == None:
        json_abort(400, 'Invalid Content-Type')

    title = data.get('title', None)
    if title == None:
        json_abort(400, 'Invalid request parameters')

    id = max([int(t.taskId) for t in Tasks]+[-1]) + 1
    newTask = Task(taskId=int(id), title=title, associatedList=listId)

    Tasks.append(newTask)
    return jsonify(newTask.__dict__)

if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)

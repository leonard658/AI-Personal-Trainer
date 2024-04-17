from flask import Flask, render_template, request
from PersonObject import *
from QueryGPT import *
from ParseGPTReturn import *

app = Flask(__name__)
messages = [] #holds all previous conversation to be used to be able to alter given workout plan
curUser = Person()

@app.route("/")
def selectionScreen():
    return render_template('selectionScreen.html')

@app.route("/test")
def test():
    return render_template('test2.html')

@app.route("/outputScreen", methods=['POST'])
def outputScreen():
    if len(messages) == 0:
        curUser.setName(request.form["name"])
        curUser.setAge(request.form["age"])
        curUser.setWeight(request.form["weight"])
        curUser.setHeight(request.form["height"])
        curUser.setCurFitnessLevel(request.form["fitnessLevel"])
        curUser.setInjuries(request.form["injuries"])
        curUser.setTime(request.form["time"])
        curUser.setGoals(request.form["goals"])
        curUser.setFocus(request.form["focus"])
        output = QueryGPT(curUser, messages, "")
        #print(messages)
        WorkoutPlan = ParseGPTReturn(output)  
        return render_template("outputScreen.html", workout=WorkoutPlan, name=curUser.getName())
    else:
        modify = request.form["edit"]
        output = QueryGPT(curUser, messages, modify)
        #print(messages)
        WorkoutPlan = ParseGPTReturn(output)    
        return render_template("outputScreen.html", workout=WorkoutPlan, name=curUser.getName())

if __name__ == "__main__":
    app.run(debug=True)
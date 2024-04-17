class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.weight = None
        self.height = None
        self.curFitnessLevel = None #1-10 scale
        self.injuries = None #list of all injuries 
        self.time = None #time for given workout (in minutes)
        self.goals = None # list of specfic fitness goals (building muscle, being healthier...)
        self.focus = None # what muscle group is being targeted in current workout

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age
    
    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight
    
    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height
    
    def setCurFitnessLevel(self, curFitnessLevel):
        self.curFitnessLevel = curFitnessLevel

    def getCurFitnessLevel(self):
        return self.curFitnessLevel
    
    def setInjuries(self, injuries):
        self.injuries = injuries

    def getInjuries(self):
        return self.injuries
    
    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time
    
    def setGoals(self, goals):
        self.goals = goals

    def getGoals(self):
        return self.goals
    
    def setFocus(self, focus):
        self.focus = focus

    def getFocus(self):
        return self.focus
  
    def myfunc(abc):
        print("Hello my name is " + str(abc.weight))
        #print("I weigh " + abc.weight)

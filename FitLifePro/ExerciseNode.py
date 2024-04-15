class ExerciseNode:
    def __init__(self):
        self.name = None
        self.sets = None
        self.reps = None
        self.musclesHit = None
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setSets(self, sets):
        self.sets = sets
    def getSets(self):
        return self.sets
    def setReps(self, reps):
        self.reps = reps
    def getReps(self):
        return self.reps
    def setMuschlesHit(self, musclesHit):
        self.musclesHit = musclesHit
    def getMusclesHit(self):
        return self.musclesHit

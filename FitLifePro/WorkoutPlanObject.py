from ExerciseNode import ExerciseNode
class WorkoutPlan:    
    def __init__(self):
        self.warmup = None
        self.cooldown = None
        self.exercises = []
    
    def setWarmup(self, warmup):
        self.warmup = warmup
    def getWarmup(self):
        return self.warmup
    
    def setCooldown(self, cooldown):
        self.cooldown = cooldown
    def getCoolDown(self):
        return self.cooldown
    
    def addExercise(self, exercise):
        self.exercises.append(exercise)
    def popExercise(self):
        return self.exercises.pop(0)
    def workoutLength(self):
        return len(self.exercises)
        
    
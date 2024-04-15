from ExerciseNode import ExerciseNode
from WorkoutPlanObject import WorkoutPlan
    
exampleOutput = """Warm up: 5 minutes of light cardio to increase heart rate and blood flow.

ExerciseName: Pull-ups
NumberOfSets: 4
NumberOfReps: 8-10
WhatMusclesItTargets: Back, biceps

ExerciseName: Seated Row
NumberOfSets: 3
NumberOfReps: 12-15
WhatMusclesItTargets: Back, biceps

ExerciseName: Bicep Curls
NumberOfSets: 3
NumberOfReps: 12-15
WhatMusclesItTargets: Biceps

ExerciseName: Deadlifts
NumberOfSets: 4
NumberOfReps: 8-10
WhatMusclesItTargets: Back, hamstrings

ExerciseName: Bent Over Rows
NumberOfSets: 3
NumberOfReps: 12-15
WhatMusclesItTargets: Back, biceps

Cooldown: 5 minutes of stretching to improve flexibility and prevent injury.

##ENDOFPLAN##"""

def ParseGPTReturn(gptOutput):
    workoutPlan = WorkoutPlan()
    allLines = gptOutput.splitlines()
    #print(allLines)
    while len(allLines) > 0:
        str = allLines.pop(0)
        if len(str) > 1:
            curStart = str.split(": ")
            #print(curStart)
            tag = curStart.pop(0)
            if tag == "Warm up":
                workoutPlan.setWarmup(curStart.pop(0))
                #print(workoutPlan.getWarmup())
            elif tag == "ExerciseName":
                tempNode = ExerciseNode()
                tempNode.setName(curStart.pop(0))
                tempNode.setSets(allLines.pop(0).split(": ").pop(1))
                tempNode.setReps(allLines.pop(0).split(": ").pop(1))
                tempNode.setMuschlesHit(allLines.pop(0).split(": ").pop(1))
                workoutPlan.addExercise(tempNode)
            elif tag == "Cooldown":
                workoutPlan.setCooldown(curStart.pop(0))
    return workoutPlan
        
        
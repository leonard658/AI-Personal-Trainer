import unittest
from PersonObject import *
from ExerciseNode import *
from ParseGPTReturn import *
from WorkoutPlanObject import *

class TestObjects(unittest.TestCase):

    def test_PersonObject(self):
        curUser = Person()
        curUser.setName("bob")
        curUser.setAge("18")
        curUser.setWeight("200")
        curUser.setHeight("70")
        curUser.setCurFitnessLevel("5")
        curUser.setInjuries("none")
        curUser.setTime("60")
        curUser.setGoals("bodybuilding")
        curUser.setFocus("back and biceps")
        self.assertEqual(curUser.getName(), "bob")
        self.assertEqual(curUser.getAge(), "18")
        self.assertEqual(curUser.getWeight(), "200")
        self.assertEqual(curUser.getHeight(), "70")
        self.assertEqual(curUser.getCurFitnessLevel(), "5")
        self.assertEqual(curUser.getInjuries(), "none")
        self.assertEqual(curUser.getTime(), "60")
        self.assertEqual(curUser.getGoals(), "bodybuilding")
        self.assertEqual(curUser.getFocus(), "back and biceps")

    def test_ExerciseNode(self):
        temp = ExerciseNode()
        temp.setName("Pull-up")
        temp.setSets("4")
        temp.setReps("12")
        temp.setMuschlesHit("back and biceps")
        self.assertEqual(temp.getName(), "Pull-up")
        self.assertEqual(temp.getSets(), "4")
        self.assertEqual(temp.getReps(), "12")
        self.assertEqual(temp.getMusclesHit(), "back and biceps")

    def test_parseGPTReturnAndWorkoutPlan(self):
        workout = WorkoutPlan()
        workout = ParseGPTReturn("""Warm up: 5 minutes of light cardio to increase heart rate and blood flow.

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

##ENDOFPLAN##""")
        self.assertEqual('5 minutes of light cardio to increase heart rate and blood flow.', workout.getWarmup())
        self.assertEqual('5 minutes of stretching to improve flexibility and prevent injury.', workout.getCoolDown())
        self.assertEqual(5, workout.workoutLength())

unittest.main()


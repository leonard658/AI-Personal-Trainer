import openai
from PersonObject import Person

openai.api_key = "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"
def QueryGPT(curUser, messages):
    if len(messages) == 0:
        gptInput = """You are a great personal trainer who likes to help their clients develop a workout plan that allows them to reach their fitness goals as fast as possible. 
I will give you a client's: 
Age - Please accommodate older and younger clients.
Current weight-  (in pounds)
Current height- (in inches)
Fitness level(on a scale of 1-10, 1 being worst, 10 being best) - if they are heavy relative to their height and out of shape make sure that you keep this in mind). If they are in very good shape, feel free to add more/more difficult exercises that still would fit in the given time frame.
Personal goals - what they want to accomplish by going to the gym consistently.
Current injuries - you must make sure you accommodate injuries when making the plan.
Time - amount of time to complete their workout in minutes.
Focus – what muscle groups they plan to target for their current workout.

From this information please produce a personalized workout (with the number of total exercises determined by personal information) plan in the following format. Make sure that there are no extra sections or any extra information about the exercise that I don't ask for. 
Warm up: Short description of a good warm up (fits on one line).
ExerciseName: (fits on one line)
NumberOfSets: (fits on one line)
NumberOfReps: (fits on one line)
WhatMusclesItTargets: (fits on one line and just lists muscle groups)
Cooldown: Short description of a good cooldown (fits on one line).
On the line below the Cooldown line include: ##ENDOFPLAN##
Make sure that there are no extra sections or any extra information about the exercise that I don't ask for.
Here is an example of the format you should use for the output)
Warm up: short description of a warmup that fits on one line

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

Cooldown: short description of a cooldown that fits on one line

##ENDOFPLAN##

Personal Informations:
Age- """
        gptInput += curUser.getAge() + "\n"
        gptInput += "Current weight- " + curUser.getWeight() + "\n"
        gptInput += "Current height - " + curUser.getHeight() + "\n"
        gptInput += "Fitness level- " + curUser.getCurFitnessLevel() + "\n"
        gptInput += "Current injuries- " + curUser.getInjuries() + "\n"
        gptInput += "Time- " + curUser.getTime() + "\n"
        gptInput += "Focus- " + curUser.getFocus() + "\n"
        messages.append({"role": "user", "content": gptInput})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":gptInput}])
        output = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": output})
        print(output)
    else:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        output = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": output})
    return output

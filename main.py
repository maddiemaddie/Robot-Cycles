#This program is designed to show the actions to take during FRC Infinite Recharge
IntakeBallFromFloor = { 
    "Category" : "Intake",
    "Number" : 1,
    "Time": 1
  } #Each discrete action is stored in a dictionary
IntakeBallFromUpperHPS = {
    "Category" : "Intake",
    "Number" : 2,
    "Time": 1
  }
IntakeBallFromLowerHPS = {
    "Category" : "Intake",
    "Number" : 3,
    "Time": 1 
  }
IntakeBallFromRen = {
    "Category" : "Intake",
    "Number" : 4,
    "Time" : 1
}
IntakeBallFromTrench ={
  "Category" : "Intake",
  "Number" : 5,
  "Time" : 1
}
actions = {
  "IntakeBallFromFloor" : IntakeBallFromFloor,
  "IntakeBallFromUpperHPS" : IntakeBallFromUpperHPS,
  "IntakeBallFromLowerHPS" : IntakeBallFromLowerHPS,
  "IntakeBallFromRen" : IntakeBallFromRen,
  "IntakeBallFromTrench" : IntakeBallFromTrench
} #The individual dictionaries are combined into one
for y in actions:
  print(y)
for x, y in actions.items():
  print(x, y)
#Variables are set to hold the time value for each action
floor_t = IntakeBallFromFloor.get("Time")
uhps_t = IntakeBallFromUpperHPS.get("Time")
lhps_t = IntakeBallFromLowerHPS.get("Time")
ren_t = IntakeBallFromRen.get("Time")
trench_t = IntakeBallFromTrench.get("Time")

intake_t = [floor_t, uhps_t, lhps_t, ren_t, trench_t]

def intake_math():
  rand_intake = intake_t[2]
  print(rand_intake)
  while rand_intake < 8:
    rand_intake += 1
    print(rand_intake)
intake_math()
IntakeBallFromFloor = {
    "Category" : "Intake",
    "Number" : 1,
    "Time": 1
  }
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

actions = {
  "IntakeBallFromFloor" : IntakeBallFromFloor,
  "IntakeBallFromUpperHPS" : IntakeBallFromUpperHPS,
  "IntakeBallFromLowerHPS" : IntakeBallFromLowerHPS
}

for x, y in actions.items():
  print(x, y)


#This program is designed to show the actions to take during FRC Infinite Recharge
IntakeBallFromFloor = { 
    'Category' : 'Intake',
    'Number' : 1,
    'Time': 1
  } #Each discrete action is stored in a dictionary
IntakeBallFromUpperHPS = {
    'Category' : 'Intake',
    'Number' : 2,
    'Time': 1
  }
IntakeBallFromLowerHPS = {
    'Category' : 'Intake',
    'Number' : 3,
    'Time': 1 
  }
IntakeBallFromRen = {
    'Category' : 'Intake',
    'Number' : 4,
    'Time' : 1
}
IntakeBallFromTrench = {
  'Category' : 'Intake',
  'Number' : 5,
  'Time' : 1
}
OutputBallToFloor = {
  'Category' : 'Output',
  'Number' : 6,
  'Time' : 1
}
OutputBallToLowGoal = {
  'Category' : 'Output',
  'Number' : 7,
  'Time' : 1
}
OutputBallToHighGoal = {
  'Category' : 'Output',
  'Number' : 8,
  'Time' : 1
}
RotateSpinnerOnce = {
  'Category' : 'Spinner',
  'Number' : 9,
  'Time' : 1
}
StopSpinner = {
  'Category' : 'Spinner',
  'Number' : 10,
  'Time' : 1
}
DetectSpinnerColor = {
  'Category' : 'Spinner',
  'Number' : 11,
  'Time' : 2
}
actions = {
  'IntakeBallFromFloor' : IntakeBallFromFloor,
  'IntakeBallFromUpperHPS' : IntakeBallFromUpperHPS,
  'IntakeBallFromLowerHPS' : IntakeBallFromLowerHPS,
  'IntakeBallFromRen' : IntakeBallFromRen,
  'IntakeBallFromTrench' : IntakeBallFromTrench,
  'OutputBallToFloor' : OutputBallToFloor,
  'OutputBallToLowGoal' : OutputBallToLowGoal,
  'OutputBallToHighGoal' : OutputBallToHighGoal,
  'RotateSpinnerOnce' : RotateSpinnerOnce,
  'StopSpinner' : StopSpinner,
  'DetectSpinnerColor' : DetectSpinnerColor
} #The individual dictionaries are combined into one

for y in actions:
  print(y)

#Variables are set to hold the time value for each action
intfloor_t = IntakeBallFromFloor.get('Time')
uhps_t = IntakeBallFromUpperHPS.get('Time')
lhps_t = IntakeBallFromLowerHPS.get('Time')
ren_t = IntakeBallFromRen.get('Time')
trench_t = IntakeBallFromTrench.get('Time')
#Begin Output Time Variables
outfloor_t = OutputBallToFloor.get('Time')
outlow_t = OutputBallToLowGoal.get('Time')
outhigh_t = OutputBallToHighGoal.get('Time')
#Spinner Time Variables
rotate_t = RotateSpinnerOnce.get('Time')
stopspin_t = StopSpinner.get('Time')
detectspin_t = DetectSpinnerColor.get('Time')

intake_t = [intfloor_t, uhps_t, lhps_t, ren_t, trench_t]
output_t = [outfloor_t, outlow_t, outhigh_t]
spinner_t = [rotate_t, stopspin_t, detectspin_t]

choice = input()
if choice in actions:
  print(choice)
elif choice in combinations:
   print(choice)

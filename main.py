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
DetectGoals = {
  'Category' : 'Sensor',
  'Number' : 12,
  'Time' : 2
}
DetectHPS = {
  'Category' : 'Sensor',
  'Number' : 13,
  'Time' : 2
}
Deploy = {
  'Category' : 'Climbing',
  'Number' : 14,
  'Time' : 2
}
AttachToBar = {
  'Category' : 'Climbing',
  'Number' : 15,
  'Time' : 1
}
MoveUp = {
  'Category' : 'Climbing',
  'Number' : 16,
  'Time' : 3
}
DriveAutoLine = {
  'Category' : 'Drive',
  'Number' : 17,
  'Time' : 2
}
DriveRenBarrier = {
  'Category' : 'Drive',
  'Number' : 18,
  'Time' : 1
}
DriveTrench = {
  'Category' : 'Drive',
  'Number' : 19,
  'Time' : 1
}
DriveGoalToHPS = {
  'Category' : 'Drive',
  'Number' : 20,
  'Time' : 5
}
DriveHPSToGoal = {
  'Category' : 'Drive',
  'Number' : 21,
  'Time' : 5
}
DriveRenToGoal = {
  'Category' : 'Drive',
  'Number' : 22,
  'Time' : 3
}
DriveGoalToRenPerimeter = {
  'Category' : 'Drive',
  'Number' : 23,
  'Time' : 3
}
DriveTrenchToGoal = {
  'Category' : 'Drive',
  'Number' : 24,
  'Time' : 3
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
  'DetectSpinnerColor' : DetectSpinnerColor,
  'DetectGoals' : DetectGoals,
  'DetectHPS' : DetectHPS,
  'Deploy' : Deploy,
  'AttachToBar' : AttachToBar,
  'MoveUp' : MoveUp,
  'DriveGoalToRenPerimeter' : DriveGoalToRenPerimeter,
  'DriveAutoLine' : DriveAutoLine,
  'DriveRenBarrier' : DriveRenBarrier,
  'DriveTrench' : DriveTrench,
  'DriveGoalToHPS' : DriveGoalToHPS,
  'DriveHPSToGoal' : DriveHPSToGoal,
  'DriveRenToGoal' : DriveRenToGoal,
  'DriveGoalToRenPerimeter' : DriveGoalToRenPerimeter,
  'DriveTrenchToGoal' : DriveTrenchToGoal
}#The individual dictionaries are combined into one

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
#Sensor Time Variables
detectgoals_t = DetectGoals.get('Time')
detectHPS_t = DetectHPS.get('Time')
#Climbing Time Variables
deploy_t = Deploy.get('Time')
attachtobar_t = AttachToBar.get('Time')
moveup_t = MoveUp.get('Time')
#Drive Time Variables
goaltorenperimeter_t = DriveGoalToRenPerimeter.get('Time')

ParkRobot = {
  #'DriveGoalToRenPerimeter' : DriveGoalToRenPerimeter,
  #'IntakeBallFromFloor' : IntakeBallFromFloor,
  'Time' : (goaltorenperimeter_t + intfloor_t),
  'Points' : 5
}
HangRobot = {
#'IntakeBallFromUpperHPS' : IntakeBallFromUpperHPS,
#'Deploy' : Deploy,
#'AttachToBar' : AttachToBar,
#'MoveUp' : MoveUp,
#'DriveGoalToRenPerimeter' : DriveGoalToRenPerimeter,
'Time' : (intfloor_t + deploy_t + attachtobar_t + moveup_t + goaltorenperimeter_t),
'Points' : 25
}
combinations = {
  'ParkRobot' : ParkRobot,
  'HangRobot' : HangRobot
}
for y in ParkRobot:
  print(ParkRobot.get('Time'))

for y in actions:
  print(y)
for y in combinations:
  print(y)
intake_t = [intfloor_t, uhps_t, lhps_t, ren_t, trench_t]
output_t = [outfloor_t, outlow_t, outhigh_t]
spinner_t = [rotate_t, stopspin_t, detectspin_t]

#def intake_math():
 # rand_intake = intake_t[2]
  #while rand_intake < 8:
  #  rand_intake += 1
   # print(rand_intake)
#intake_math()

#choice = input()
#if choice in actions:
 # print(choice)
#elif choice in combinations:
 #  print(choice)
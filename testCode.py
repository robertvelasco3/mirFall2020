from mirConnection import mirConnection
from motorControl import motorControl

# mission_id for methods GoToA and GoToStart for mir
GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
GoToStart = "94601816-0363-11eb-99a6-000129922c9e"

def Dock():
    print('Currently docking the MiR100')
    mir.performMission(GoToA)

def Unload():
    print('Currently unloading the MiR100')
    motor.moveForward(5)

def Stop():
    print('Currently stopping the unloading of the MiR100')
    motor.stop()

def Load():
    print('Currently loading the MiR100')
    motor.moveBackward(2)

def Undock():
    print('Currently undocking the MiR100')
    mir.performMission(GoToStart)


mir = mirConnection()
motor = motorControl()

print('Program is running!')
while(True):
    command = input()
    if command == 'dock':
        Dock()
    elif command == 'unload':
        Unload()
    elif command == 'stop':
        Stop()
    elif command == 'load':
        Load()
    elif command == 'undock':
        Undock()
    elif command == 'end':
        print('Ending Code')
        break
    else:
        print('Error: command not valid')

motor.cleanUp()
#### obsolete, use mirControl.py instead

from mirConnection import mirConnection
from motorControl import motorControl
from time import sleep

# mission_id for methods GoToA, GoToStart, and GoToSafe for mir
GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
GoToStart = "94601816-0363-11eb-99a6-000129922c9e"
GoToSafe = "130b5cac-17dc-11eb-89d2-000129922c9e"

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

def Docking():
    Dock()
    sleep(1)
    stopped = False
    while(True):
        dist, error = mir.getDistFromTarget()
        if error:
            handleError()
            break
        if dist < 2.1 and not stopped:
            mir.deleteMissions()
            Dock()
            stopped = True
        elif dist == 0:
            break
        else:
            print('not there')

def handleError():
    mir.clearError()
    mir.makeReady()
    mir.performMission(GoToSafe)

mir = mirConnection()
motor = motorControl()

print('Program is running!')

previous = None
hasDocked = False
end = False
command = ''
hasDocked = False
while(True):
    command = input()
    if command == 'dock' and command != previous and not hasDocked:
        #mir.endMission(GoToA)
        #Dock()
        print("Im here")
    elif command == 'unload':
        Unload()
    elif command == 'stop':
        Stop()
    elif command == 'load':
        Load()
    elif command == 'undock' and command != previous:
        Undock()
    elif command == 'go':
        Docking()
    elif end:
        print('Ending Code')
        break
    else:
        print('Error: command not valid')
    previous = command
    print("hasDocked:", hasDocked)

motor.cleanUp()
from mirConnection import mirConnection
from motorControl import motorControl

#motor = motorControl()

def Dock():
    print('Currently docking the MiR100')
    mir.goToA()

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
    mir.goToStart()


mir = mirConnection()
motor = motorControl()

#mir.test()
print('Program is running!')
command = 'temp'
while(command != 'End'):
    command = input()
    if command == 'dock':
        Dock()
    elif command == 'unload' or command == 'Unload':
        Unload()
    elif command == 'stop' or command == 'Stop':
        Stop()
    elif command == 'load' or command == 'Load':
        Load()
    elif command == 'undock':
        Undock()
    else:
        print('Error: command not valid')

motor.cleanUp()
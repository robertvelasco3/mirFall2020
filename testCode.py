from mirConnection import mirConnection
from motorControl import motorControl

#motor = motorControl()

def Dock():
    print('Currently docking the MiR100')

def Unload():
    print('Currently unloading the MiR100')
    motor.moveForward(5)

def Stop():
    print('Currently stopping the unloading of the MiR100')

def Load():
    print('Currently loading the MiR100')
    motor.moveBackward(2)

def Undock():
    print('Currently undocking the MiR100')


mir = mirConnection()
motor = motorControl()

#mir.test()
print('Program is running!')
for x in range(0, 5):
    command = input()
    if command == 'Dock':
        Dock()
    elif command == 'Unload':
        Unload()
    elif command == 'Stop':
        Stop()
    elif command == 'Load':
        Load()
    elif command == 'Undock':
        Undock()
    else:
        print('Error: command not valid')

motor.stop()
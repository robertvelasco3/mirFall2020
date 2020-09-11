def Dock():
    print('Currently docking the MiR100')

def Unload():
    print('Currently unloading the MiR100')

def Stop():
    print('Currently stopping the unloading of the MiR100')

def Load():
    print('Currently loading the MiR100')

def Undock():
    print('Currently undocking the MiR100')

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
from mirConnection import mirConnection
from motorControl import motorControl
from time import sleep

class mirControl:
    '''Class used for parsing the command string and controling the mir100 robot and belt conveyer motor'''

    def __init__(self):
        # mission_id for methods GoToA, GoToStart, and GoToSafe for mir
        self.GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
        self.GoToStart = "94601816-0363-11eb-99a6-000129922c9e"
        self.GoToSafe = "130b5cac-17dc-11eb-89d2-000129922c9e"
        self.mir = mirConnection()
        self.motor = motorControl()

        self.previous = None
        self.hasDocked = False
        self.end = False
        self.command = ''
        self.hasDocked = False

    def Dock(self):
        print('Currently docking the MiR100')
        self.mir.performMission(self.GoToA)

    def Unload(self):
        print('Currently unloading the MiR100')
        self.motor.moveForward(5)

    def Stop(self):
        print('Currently stopping the unloading of the MiR100')
        self.motor.stop()

    def Load(self):
        print('Currently loading the MiR100')
        self.motor.moveBackward(2)

    def Undock(self):
        print('Currently undocking the MiR100')
        self.mir.performMission(self.GoToStart)

    def Docking(self):
        self.Dock()
        sleep(1)
        stopped = False
        while(True):
            dist, error = self.mir.getDistFromTarget()
            if error:
                self.handleError()
                break
            if dist < 2.1 and not stopped:
                self.mir.deleteMissions()
                self.Dock()
                stopped = True
            elif dist == 0:
                break
            else:
                print('not there')

    def handleError(self):
        self.mir.clearError()
        self.mir.makeReady()
        self.mir.performMission(self.GoToSafe)

    def processCommand(self, command):
        '''Process incomming command string and run once accordingly'''
        if command == 'dock' and command != self.previous and not self.hasDocked:
            #mir.endMission(GoToA)
            #Dock()
            print("Im here")
        elif command == 'unload':
            self.Unload()
        elif command == 'stop':
            self.Stop()
        elif command == 'load':
            self.Load()
        elif command == 'undock' and command != self.previous:
            self.Undock()
        elif command == 'go':
            self.Docking()
        elif self.end:
            print('Ending Code')
            return False
        else:
            print('Error: command not valid')
        self.previous = command
        print("hasDocked:", self.hasDocked)
        return True

if __name__ == '__main__':
    mirCtrl = mirControl()
    while (True):
        cmd = input()
        if not mirCtrl.processCommand(cmd):
            break

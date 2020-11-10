from mirConnection import mirConnection
from motorControl import motorControl
from time import sleep

class mirControl:
    '''Class used for parsing the command string and controling the mir100 robot and belt conveyer motor'''

    def __init__(self, mir = mirConnection()):
        # mission_id for methods GoToA, GoToStart, and GoToSafe for mir
        self.GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
        self.GoToStart = "94601816-0363-11eb-99a6-000129922c9e"
        self.GoToSafe = "130b5cac-17dc-11eb-89d2-000129922c9e"
        self.mir = mir
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

#Inputs: None
#outpus: None
#description: performs regular dock until the distance from target is 2.1 meters away.
#             Then it stops and continues docking process. If there are any errors, it calls handle error.
#             Path count is a variable that increments when the path length changes. Once path count gets
#.            to 4 (we assume path is unreachable) missions are deleted from the queue and the error handler is called.
    def Docking(self):
        pathCount = 0
        self.Dock()
        sleep(0.1)
        stopped = False
        oldDist = 10000
        while(True):
            sleep(0.2)
            dist, error = self.mir.getDistFromTarget()
            if error:
                self.handleError()
                break
            if dist > (oldDist + 0.5):
                pathCount += 1
                print("MiR altered its path. pathCount = ", pathCount)
            if dist < 2.1 and not stopped:
                self.mir.deleteMissions()
                self.Dock()
                stopped = True
            elif dist == 0:
                break
            else:
                print('not there')
            oldDist = dist
            if(pathCount == 4):
                print("Error: Path changed ", pathCount, " times. Stopping program to avoid endless loop.")
                self.mir.deleteMissions()
                self.handleError()
                break

    def handleError(self):
        self.mir.clearError()
        self.mir.makeReady()
        self.mir.performMission(self.GoToSafe)

    def processCommand(self, command):
        '''Process incomming command string and run once accordingly'''
        #if command == 'dock' and command != self.previous and not self.hasDocked:
            #mir.endMission(GoToA)
            #Dock()
            #print("Im here")
        if command == 'unload':
            self.Unload()
        elif command == 'stop':
            self.Stop()
        elif command == 'load':
            self.Load()
        elif command == 'undock' and command != self.previous:
            self.Undock()
        elif command == 'dock':
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

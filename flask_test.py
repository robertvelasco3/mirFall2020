from flask import Flask
import threading
from mirConnection import mirConnection
from motorControl import motorControl
from time import sleep


GoToA = "cfbc2ff2-0363-11eb-99a6-000129922c9e"
GoToStart = "94601816-0363-11eb-99a6-000129922c9e"

mir = mirConnection()
motor = motorControl()

previous = None
hasDocked = False
end = False
command = ''
hasDocked = False


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
    while(True):
        if mir.getDistFromTarget() < 2.1:
            break
        else:
            print('not there')
    mir.deleteMissions()
    Dock()


app = Flask(__name__)
startE = threading.Event()
stopE = threading.Event()
endE = threading.Event()


@app.route("/start")
def start():
    startE.set()
    return "Start Done"

    
@app.route("/stop")
def stop():
    stopE.set()
    startE.clear()
    return "Stop Done"

@app.route("/end")
def end():
    stopE.set()
    startE.clear()
    endE.set()
    return "Stop Done"

def work_in_loop():
    command = input()
    if command == 'dock' and command != previous and not hasDocked:
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
    #elif end:
      #  print('Ending Code')
        
    else:
        print('Error: command not valid')
    previous = command
    print (command)
    print("hasDocked:", hasDocked)

def work_setup():
    print('Program is running!')
    #previous = None
    #hasDocked = False
    #end = False
    #command = ''
    #hasDocked = False

def work_end():
    Undock()
    motor.cleanUp()

def work_pause():
    pass


def worker():
    work_setup()
    while True:
        startE.wait()
        if (endE.isSet()):
            work_end()
            break
        print ("starting")
        while True:
            work_in_loop()
            if stopE.isSet():
                print ("stopping")
                stopE.clear()
                work_pause()
                break

def flask_run():
    app.run(host="localhost", port="1234", debug=False)

if __name__ == '__main__':
    startE.clear()
    stopE.clear()
    endE.clear()
    t = threading.Thread(target=flask_run)
    t.start()
    worker()
    

from flask import Flask
from mirControl import mirControl
import threading
import sys, termios
import time
import Queue

class mirControlThread:
    '''Thread control to pause and resume mir script, controled by client HTTP request'''
    ### we will not end the service! as we cannot terminate flask
    def __init__(self):
        self.pauseE = threading.Event()
        self.pauseE.set()
        self.mirCtrl = mirControl()
        self.timeout = 5
        self.tick = 0.2 #may not need this if script reacts too slow
        self.curTime= time.time()
        self.inputTime = self.curTime
        self.inputCommand = None

    def inputProducer(self):
        '''We are only interested in the most recent command as it should only change after mir acted to it'''
        while True:
            cmd = input()
            self.inputCommand = cmd
            self.inputTime = time.time()

    def resume(self):
        self.pauseE.clear()
        self.curTime= time.time()

    def pause(self):
        self.pauseE.set()

    def handleError(self):
        #Read network, mir status, take action if necessary
        pass

    def run(self):
        t = threading.Thread(target=self.inputProducer)
        t.start()
        while(True):
            time.sleep(self.tick)
            if self.pauseE.isSet():
                continue
            self.handleError()
            if self.inputTime > self.curTime:
                self.mirCtrl.processCommand(self.inputCommand)
                self.curTime = self.inputTime

mct = mirControlThread()
app = Flask(__name__)

@app.route("/resume")
def resume():
    mct.resume()
    return '{"res":"Running"}'

    
@app.route("/pause")
def pause():
    mct.pause()
    return '{"res":"Paused"}'

def flask_run():
    app.run(host="localhost", port="1234", debug=False)

if __name__ == '__main__':
    t = threading.Thread(target=flask_run)
    t.start()
    mct.run()
    exit(2)
    

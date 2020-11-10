from flask import Flask
from mirControl import mirControl
from mirConnection import mirConnection
import threading
import sys
import time

class mirControlThread:
    '''Thread control to pause and resume mir script, controled by client HTTP request'''
    ### we will not end the service! as we cannot terminate flask
    def __init__(self):
        self.pauseE = threading.Event()
        self.pauseE.set()
        self.mirCon = mirConnection() 
        self.mirCtrl = mirControl(mir = self.mirCon)
        self.timeout = 5
        self.tick = 0.2 #may not need this if script reacts too slow
        self.curTime= time.time()
        self.inputTime = self.curTime
        self.inputCommand = None
        self.error = False
        self.errorJSON = None

    def inputProducer(self):
        '''We are only interested in the most recent command as it should only change after mir acted to it'''
        while True:
            cmd = input()
            self.inputCommand = cmd
            self.inputTime = time.time()

    def resume(self):
        print("resume called")
        if self.error:
            return self.errorJSON
        self.pauseE.clear()
        self.curTime= time.time()
        return '{"res":"Running"}'

    def pause(self):
        print("pause called")
        if self.error:
            return self.errorJSON
        self.pauseE.set()
        return '{"res":"Paused"}'

    def handleError(self):
        #Read network, mir status, take action if necessary
        req, status = self.mirCon.getStatusText()
        while req.status >299 or req.status < 200:
            #lost connection, nothing we can really do
            self.errorJSON = '{"Res":"MiR Lost Connection"}'
            self.error = True
            print("Connection Lost!!!")
            time.sleep(self.tick*3)
            req, status = self.mirCon.getStatusText()
        if (len(status['errors']) != 0):
            print(status['errors'])
        

    def run(self):
        t = threading.Thread(target=self.inputProducer)
        t.start()
        self.pauseE.wait()
        self.mirCtrl.processCommand("dock")
        while(True):
            time.sleep(self.tick)
            if self.pauseE.isSet():
                continue
            self.handleError()
            if self.inputTime > self.curTime:
                print (self.inputCommand)
                self.mirCtrl.processCommand(self.inputCommand)
                self.curTime = self.inputTime

mct = mirControlThread()
app = Flask(__name__)

@app.route("/resume")
def resume():
    return mct.resume()

@app.route("/pause")
def pause():
    return mct.pause()
    

def flask_run():
    app.run(host="localhost", port="1234", debug=False)

if __name__ == '__main__':
    t = threading.Thread(target=flask_run)
    t.start()
    mct.run()
    exit(2)
    

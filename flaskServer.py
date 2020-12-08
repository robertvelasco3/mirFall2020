from flask import Flask
from flask_cors import CORS
from mirControl import mirControl
from mirConnection import mirConnection
import threading
import sys, os
import subprocess
import time

class mirControlThread:
    '''Thread control to pause and resume mir script, controled by client HTTP request'''
    ### we will not end the service! as we cannot terminate flask

    def __init__(self):
        "initialize newlly created class with default values"
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
        self.errorMSG = " "
        self.atStart = True
        self.statusMSG = " "

    def inputProducer(self):
        '''Thread to accept input from standard input (QR scanner) with timestamp'''
        #input() blocks the program from running so this has to be made asynchronic 
        # so we have a chance to do something else in the main control thread.
        #We are only interested in the most recent command as it should only change after mir acted to it
        while True:
            cmd = input()
            self.inputCommand = cmd
            self.inputTime = time.time()

    def resume(self):
        '''Asynchronic call to resume the control thread'''
        #print("resume called")
        if self.error:
            return self.errorMSG
        if self.atStart:
            self.inputCommand = "dock"
            self.inputTime = time.time()#set time so script ignores old input
            if not self.pauseE.is_set():
                self.pauseE.set()
            return "Parts delivering!"
        elif self.pauseE.is_set():
            return "Already delivering!"
        else:
            self.pauseE.set()
            self.curTime= time.time()#set time so script ignores old input
        return "Resuming!"

    def pause(self):
        '''Asynchronic call to pause the control thread'''
        #print("pause called")
        if self.error:
            return self.errorMSG
        if not self.pauseE.is_set():
            return "Already Paused!"
        self.pauseE.clear()
        return "Pausing program..."

    def safe(self):
        if self.mirCtrl.safe():
            return "Resuming from safety location"
        else:
            return "Not at safety location"

    def status(self):
        if self.error:
            return self.errorMSG
        return self.statusMSG + ", Location: " + self.mirCtrl.getLocation() + ", Action: " + self.mirCtrl.getAction()

    def handleError(self):
        '''Uses mir control class to communicate with mir to see if error exitst'''
        #Read network, mir status, take action if necessary
        req, status = self.mirCon.getStatusText()
        while req.status >299 or req.status < 200:
            #lost connection, nothing we can really do
            self.errorMSG = "MiR Lost Connection: "
            self.error = True
            print("Connection Lost!!!")
            time.sleep(self.tick*3)
            req, status = self.mirCon.getStatusText()
        if ('error' in status and len(status['errors']) != 0):
            print(status['errors'])
            self.errorMSG = self.errorMSG  + status['errors']
        else:
            self.statusMSG = "Battery: " + str(status["battery_percentage"])[:5]

    def run(self):
        '''Control thread that check error repeatly and calls mir control when we have new input'''
        t = threading.Thread(target=self.inputProducer) #create input thread
        t.start()
        self.pauseE.clear()
        self.pauseE.wait()
        #self.mirCtrl.processCommand("dock")
        while(True):
            time.sleep(self.tick)
            if not self.pauseE.isSet():
                #Skips following if script is paused
                continue
            self.handleError()
            if self.inputTime > self.curTime:
                print (self.inputCommand)
                self.atStart=self.mirCtrl.processCommand(self.inputCommand)
                self.curTime = self.inputTime

mct = mirControlThread()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#Flask API service calls
#forwarded into mir control thread class

@app.route("/resume")
def resume():
    return mct.resume()

@app.route("/pause")
def pause():
    return mct.pause()

@app.route("/safe")
def safe():
    return mct.safe()

@app.route("/status")
def status():
    return mct.status()
    
#flask thread
def flask_run():
    app.run(host="0.0.0.0", port="1234", debug=False)

if __name__ == '__main__':
    '''Setup flask to run in a separate thread and calls mir control thread to run'''
    #newpid = os.fork()
    #if newpid == 0:
    #    os.chdir("angularCode")
    #    os.execvp("ng", ["ng", "serve", "--port=80", "--host=0.0.0.0"])
    t = threading.Thread(target=flask_run)
    t.start()
    mct.run()
    exit(2)
    

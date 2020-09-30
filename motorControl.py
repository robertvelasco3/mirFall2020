#library
import RPi.GPIO as GPIO 
from time import sleep

#Pins 18 22 24 GPIO 24 25 8
Motor1E = 24 #  Enable pin 1 of the controller IC
Motor1A = 25 #  Input 1 of the controller IC
Motor1B = 8 #  Input 2 of the controller IC

class motorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        self.forward=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
        self.reverse=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM

        self.forward.start(0) 
        self.reverse.start(0)
    
    def moveForward(self, seconds):
        # this will run your motor in forward direction for the given amount of seconds with 50% speed.
        print("GO forward")
        GPIO.output(Motor1E,GPIO.HIGH)
        self.forward.ChangeDutyCycle(100)
        self.reverse.ChangeDutyCycle(0)
        sleep(seconds)
        self.forward.ChangeDutyCycle(0)
        self.reverse.ChangeDutyCycle(0)
        
    def moveBackward(self,seconds):
        # this will run your motor in reverse direction for the given amount of seconds with 80% speed by supplying 80% of the battery voltage
        print("GO backward")
        GPIO.output(Motor1E,GPIO.HIGH)
        self.forward.ChangeDutyCycle(0)
        self.reverse.ChangeDutyCycle(100)
        sleep(seconds)
        self.forward.ChangeDutyCycle(0)
        self.reverse.ChangeDutyCycle(0)
    
    def stop(self):
        #stop motor
        print("Now stop")
        GPIO.output(Motor1E,GPIO.LOW)
        self.forward.stop() # stop PWM from GPIO output it is necessary
        self.reverse.stop() 

        GPIO.cleanup()












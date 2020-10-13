#library
import RPi.GPIO as GPIO 
from time import sleep

#Pins 18 22 24 GPIO 24 25 8
Motor1E = 24 # Enable pin 1 of the controller IC
Motor1A = 25 # Input 1 of the controller IC
Motor1B = 8  # Input 2 of the controller IC

Motor2E = 11 # Enable pin for motor 2
Motor2A = 10 # Input 1 for motor 2
Motor2B = 22 # Input 2 for motor 2

class motorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
        
        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)

        self.forward1=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
        self.reverse1=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM
        
        self.forward2=GPIO.PWM(Motor2A,100) # configuring Enable pin for PWM
        self.reverse2=GPIO.PWM(Motor2B,100) # configuring Enable pin for PWM

        self.forward1.start(0) 
        self.reverse1.start(0)
        
        self.forward2.start(0)
        self.reverse2.start(0)
    
    def moveForward(self, seconds):
        # this will run both motors in the forward direction with 100% speed.
        print("Move both motors forward")
        GPIO.output(Motor1E,GPIO.HIGH)
        self.forward1.ChangeDutyCycle(100)
        self.reverse1.ChangeDutyCycle(0)
        
        GPIO.output(Motor2E,GPIO.HIGH)
        self.forward2.ChangeDutyCycle(100)
        self.reverse2.ChangeDutyCycle(0)
        
    def moveBackward(self,seconds):
        # this will run both motors in reverse with 100% speed.
        print("Move both motors backward")
        GPIO.output(Motor1E,GPIO.HIGH)
        self.forward1.ChangeDutyCycle(0)
        self.reverse1.ChangeDutyCycle(100)
        
        GPIO.output(Motor2E,GPIO.HIGH)
        self.forward2.ChangeDutyCycle(0)
        self.reverse2.ChangeDutyCycle(100)
    
    def stop(self):
        self.forward1.ChangeDutyCycle(0)
        self.reverse1.ChangeDutyCycle(0)
        
        self.forward2.ChangeDutyCycle(0)
        self.reverse2.ChangeDutyCycle(0)
    
    def cleanUp(self):
        #stop motor
        print("Clean Up GPIO Pins")
        GPIO.output(Motor1E,GPIO.LOW)
        self.forward1.stop() # stop PWM from GPIO output it is necessary
        self.reverse1.stop()
        
        GPIO.output(Motor2E,GPIO.LOW)
        self.forward2.stop() # stop PWM from GPIO output it is necessary
        self.reverse2.stop() 

        GPIO.cleanup()

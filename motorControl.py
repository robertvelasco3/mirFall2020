#library
import RPi.GPIO as GPIO 
from time import sleep

class motorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #Pins 18 22 24 GPIO 24 25 8
        Motor1E = 24 #  Enable pin 1 of the controller IC
        Motor1A = 25 #  Input 1 of the controller IC
        Motor1B = 8 #  Input 2 of the controller IC

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        forward=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
        reverse=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM

        forward.start(0) 
        reverse.start(0)
    
    def moveForward(seconds):
        # this will run your motor in forward direction for the given amount of seconds with 50% speed.
        print "GO forward"
        GPIO.output(Motor1E,GPIO.HIGH)
        forward.ChangeDutyCycle(50)
        reverse.ChangeDutyCycle(0)
        sleep(seconds)
        
    def moveBackward(seconds):
        # this will run your motor in reverse direction for the given amount of seconds with 80% speed by supplying 80% of the battery voltage
        print "GO backward"
        GPIO.output(Motor1E,GPIO.HIGH)
        forward.ChangeDutyCycle(0)
        reverse.ChangeDutyCycle(80)
        sleep(seconds)
    
    def stop():
        #stop motor
        print "Now stop"
        GPIO.output(Motor1E,GPIO.LOW)
        forward.stop() # stop PWM from GPIO output it is necessary
        reverse.stop() 

        GPIO.cleanup()













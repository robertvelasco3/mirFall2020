#library
import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
#Pins 18 22 24 GPIO 24 25 8
Motor1E = 24 #  Enable pin 1 of the controller IC
Motor1A = 25 #  Input 1 of the controller IC
Motor1B = 8 #  Input 2 of the controller IC

Motor2E = 11
Motor2A = 10
Motor2B = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

forward=GPIO.PWM(Motor1A,100) # configuring Enable pin for PWM
reverse=GPIO.PWM(Motor1B,100) # configuring Enable pin for PWM

forward2=GPIO.PWM(Motor2A,100) # configuring Enable pin for PWM
reverse2=GPIO.PWM(Motor2B,100) # configuring Enable pin for PWM

forward.start(0) 
reverse.start(0)

forward2.start(0)
reverse2.start(0)

# this will run your motor in reverse direction for 2 seconds with 80% speed by supplying 80% of the battery voltage
print("GO backward")
GPIO.output(Motor1E,GPIO.HIGH)
forward.ChangeDutyCycle(0)
reverse.ChangeDutyCycle(80)

GPIO.output(Motor2E,GPIO.HIGH)
forward2.ChangeDutyCycle(0)
reverse2.ChangeDutyCycle(80)


sleep(2)


# this will run your motor in forward direction for 5 seconds with 50% speed.
print("GO forward")
GPIO.output(Motor1E,GPIO.HIGH)
forward.ChangeDutyCycle(50)
reverse.ChangeDutyCycle(0)

GPIO.output(Motor2E,GPIO.HIGH)
forward2.ChangeDutyCycle(50)
reverse2.ChangeDutyCycle(0)

sleep(5)

#stop motor
print("Now stop")
GPIO.output(Motor1E,GPIO.LOW)
forward.stop() # stop PWM from GPIO output it is necessary
reverse.stop()

GPIO.output(Motor2E,GPIO.LOW)
forward2.stop() # stop PWM from GPIO output it is necessary
reverse2.stop() 


GPIO.cleanup()
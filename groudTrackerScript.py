#import os
import RPi.GPIO as GPIO
import time
import math

class bLoc:
    lat = 44.960217
    long = -93.202116
    alt = 10000

class tLoc:
    lat = 44.975055
    long = -93.233332
    alt = 830

class servoPeram:
    hAngle = 75
    vAngle = 45


def calcAngles():
    r = 20902000 #radius of earth

    a = 45
    c = 45

    d = r*c #distance across earths surface

    h = math.fabs(bLoc.alt - tLoc.alt) #differnce in height

    vAngle = 45 # vertical hAngle

    hAngle = 45 #horizontal angle



def main():

    #os.chdir("C:\\Users\\Jack Troshinsky\\Documents\\AAP\\Script")

    servoPINH = 20
    servoPINV = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINH, GPIO.OUT)
    GPIO.setup(servoPINV, GPIO.OUT)

    pH = GPIO.PWM(servoPIN, 50) # GPIO 20 for PWM with 50Hz
    pH.start(2.5) # Initialization

    pV = GPIO.PWM(servoPIN, 50) # GPIO 20 for PWM with 50Hz
    pV.start(2.5) # Initialization

    while(1):

        try:
          while True:
            pH.ChangeDutyCycle(5)
            time.sleep(0.5)
            pH.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            pH.ChangeDutyCycle(10)
            time.sleep(0.5)
            pH.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            pH.ChangeDutyCycle(10)
            time.sleep(0.5)
            pH.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            pH.ChangeDutyCycle(5)
            time.sleep(0.5)
            pH.ChangeDutyCycle(2.5)
            time.sleep(0.5)
        except KeyboardInterrupt:
          pH.stop()
          pV.stop()
          GPIO.cleanup()

        time.sleep(10)


main()



#pull in location
#determine servo settings
#move servos


#read in data
#send data

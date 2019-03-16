#import os
import RPi.GPIO as GPIO
import time
import math

class bLoc:
    lat = 44.960217
    lon = -93.202116
    alt = 10000

class tLoc:
    lat = 44.975055
    lon = -93.233332
    alt = 830

class servoPeram:
    hAngle = 75
    vAngle = 45


def calcAngles():
    r = 20902000 #radius of earth

    a = math.pow(math.sin(math.radians(bLoc.lat-tLoc.lat)/2),2) + math.cos(tLoc.lat) * math.cos(bLoc.lat) * math.pow(math.sin(math.radians(bLoc.lon-tLoc.lon)/2),2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    d = r*c #distance across earths surface

    print("Distance to baloon: " + str(d) + "ft")

    h = math.fabs(bLoc.alt - tLoc.alt) #differnce in height

    vAngle = math.atan(h/d) # vertical hAngle

    hAngle = 45 #horizontal angle

    print("Vertical angle: " + str(math.degrees(vAngle)) + " degrees")
    print("Horizantal angle: NA degrees")

    servoPeram.vAngle = (vAngle/90)*10+2.5
    print("Servo PWM Vertical: " + str(servoPeram.vAngle))



def main():

    #os.chdir("C:\\Users\\Jack Troshinsky\\Documents\\AAP\\Script")

    servoPINH = 13
    servoPINV = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINH, GPIO.OUT)
    #GPIO.setup(servoPINV, GPIO.OUT)

    pH = GPIO.PWM(servoPINH, 50) # GPIO 20 for PWM with 50Hz
    pH.start(2.5) # Initialization

    #pV = GPIO.PWM(servoPINV, 50) # GPIO 20 for PWM with 50Hz
    #pV.start(2.5) # Initialization

    calcAngles()

    while(1):

        try:
          while True:
            pH.ChangeDutyCycle(5)
            time.sleep(1)
            pH.ChangeDutyCycle(7.5)
            time.sleep(1)
            pH.ChangeDutyCycle(10)
            time.sleep(1)
            pH.ChangeDutyCycle(12.4)
            time.sleep(5)

            pH.ChangeDutyCycle(servoPeram.vAngle)
            time.sleep(5)

        except KeyboardInterrupt:
          pH.stop()
         # pV.stop()
          GPIO.cleanup()

        time.sleep(10)


main()



#pull in location
#determine servo settings
#move servos


#read in data
#send data

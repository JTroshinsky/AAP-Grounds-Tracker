#import os
import RPi.GPIO as GPIO
import time
import math

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class bLoc:
    lat = 44.960217
    lon = -93.202116
    alt = 10000

class tLoc:
    lat = 44.975009
    lon = -93.233251
    alt = 830

class servoPeram:
    hAngle = 45
    vAngle = 45


def calcAngles():

    #Vertical andgle --------------------------------------------------------
    r = 20902000 #radius of earth

    a = math.pow(math.sin(math.radians(bLoc.lat-tLoc.lat)/2),2) + math.cos(tLoc.lat) * math.cos(bLoc.lat) * math.pow(math.sin(math.radians(bLoc.lon-tLoc.lon)/2),2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    d = r*c #distance across earths surface

    print("Distance to baloon: " + str(d) + "ft")

    h = math.fabs(bLoc.alt - tLoc.alt) #differnce in height

    vAngle = math.degrees(math.atan(h/d)) # vertical hAngle in degrees

    servoPeram.vAngle = (abs(90-vAngle)/90)*9+2.5

    print("Vertical angle: " + str(vAngle) + " degrees")
    print("Servo PWM Vertical: " + str(servoPeram.vAngle) + "\n")


    #Horizantal andgle --------------------------------------------------------

    y = math.sin(math.radians(bLoc.lon-tLoc.lon)) * math.cos(math.radians(bLoc.lat))
    x = math.cos(math.radians(tLoc.lat)) * math.sin(math.radians(bLoc.lat)) -  math.sin(math.radians(tLoc.lat)) * math.cos(math.radians(bLoc.lat)) * math.cos(math.radians(bLoc.lon - tLoc.lon))

    hAngle = math.degrees(math.atan2(y,x)) #horizontal angle
    if(hAngle < 0):
        hAngle += 360

    servoPeram.hAngle = ((hAngle)/90)*10+2.5

    print("Horizantal angle: " + str(hAngle))
    print("Servo PWM Horizantal: " + str(servoPeram.hAngle))



def updateLocation():
    my_url = 'http://www.aerostatumn.org/gt.html'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html5lib")

    cordLine = str(page_soup.body.find("p", id = "cords"))
    parse = [x.strip() for x in cordLine.split(',')]

    bLoc.lat = float(parse[1])
    bLoc.lon = float(parse[2])
    bLoc.alt = float(parse[3])


def main():

    #os.chdir("C:\\Users\\Jack Troshinsky\\Documents\\AAP\\Script")

    servoPINH = 13
    servoPINV = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINH, GPIO.OUT)
    GPIO.setup(servoPINV, GPIO.OUT)

    pV = GPIO.PWM(servoPINH, 50) # GPIO 20 for PWM with 50Hz
    pV.start(2.5) # Initialization

    pH = GPIO.PWM(servoPINH, 50) # GPIO 20 for PWM with 50Hz
    pH.start(2.5) # Initialization


    calcAngles()

    while(1):

        try:
          while True:
            pV.ChangeDutyCycle(2.5)
            time.sleep(1)
            pV.ChangeDutyCycle(5)
            time.sleep(1)
            pV.ChangeDutyCycle(7.5)
            time.sleep(1)
            pV.ChangeDutyCycle(9)
            time.sleep(1)

            pV.ChangeDutyCycle(servoPeram.vAngle)
            time.sleep(5)

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

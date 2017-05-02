#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

led = [14, 15, 18, 23, 25, 8, 7, 12, 16, 20]
bottoni = [2, 21]
vel = 0.5

def __init__():
    GPIO.setmode(GPIO.BCM)
    for i in led:
        GPIO.setup(i, GPIO.OUT)
    for i in bottoni:
        GPIO.setup(i, GPIO.IN)
    GPIO.setwarnings(False)

def andata():
    for i in led:
        GPIO.output(i, 1)
    	sleep(vel)
    	GPIO.output(i, 0)
    	sleep(vel)

def ritorno():
    #led[::-1]:
    for i in reversed(led):
        GPIO.output(i, 1)
    	sleep(vel)
    	GPIO.output(i, 0)
    	sleep(vel)

def vittoriaRosso():
    for time in range(5):
        for i in led:
            GPIO.output(i, 1)
        sleep(0.2)
        for i in led:
            GPIO.output(i, 0)
        sleep(0.2)

def vittoriaVerde():
    for time in range(5):
        for i in led:
            GPIO.output(i, 1)
        sleep(0.2)
        for i in led:
            GPIO.output(i, 0)
        sleep(0.2)

def main():
    try:
        continua = True
        while(continua):
            if(GPIO.input(bottoni[1]) == 1):
                ritorno()
                if(GPIO.input(bottoni[0]) == 1):
                    andata()
                    vel -= 0.05
                else:
                    vittoriaRosso()
                    continua = False
            else:
                vittoriaVerde()
                continua = False
    except:
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        main()
    except:
        pass

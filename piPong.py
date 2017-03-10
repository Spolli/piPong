import RPi.GPIO as GPIO
from time import sleep
import sys

led = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16]
bottoni = [2, 3]

GPIO.setmode(GPIO.BCM)
for init in led:
    GPIO.setup(init, GPIO.OUT)
for init2 in bottoni:
    GPIO.setup(init2, GPIO.IN)
GPIO.setwarnings(False)

def andata():
    for i in led:
        GPIO.output(i, 1)
    	sleep(0.2)
    	GPIO.output(i, 0)
    	sleep(0.2)

def ritorno():
    for i in led[::-1]:
        GPIO.output(i, 1)
    	sleep(0.2)
    	GPIO.output(i, 0)
    	sleep(0.2)

def vittoriaRosso():
    for time in 5:
        for init in led:
            GPIO.output(init, 1)
        sleep(0.2)
        for init in led:
            GPIO.output(init, 0)
        sleep(0.2)

def vittoriaVerde():
    for time in 5:
        for init in led:
            GPIO.output(init, 1)
        sleep(0.2)
        for init in led:
            GPIO.output(init, 0)
        sleep(0.2)

continua = True
while(continua):
    if(bottoni[1] == 1 and led[led.lenght] == 1):
        ritorno()
        if(bottoni[0] == 1 and led[0] == 1):
            andata()
        else:
            vittoriaRosso()
            continua = False
    else:
        vittoriaVerde()
        continua = False

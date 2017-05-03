#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

led = [2, 3, 4, 17, 27, 22, 10, 9]
bottoni = [14, 21]
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
    # led[::-1]:
    for i in reversed(led):
        GPIO.output(i, 1)
        sleep(vel)
        GPIO.output(i, 0)
        sleep(vel)


def vittoriaRosso():
    for time in range(5):
        for init in led[4:]:
            GPIO.output(init, 1)
        sleep(0.2)
        for init in led[4:]:
            GPIO.output(init, 0)
        sleep(0.2)


def vittoriaVerde():
    for time in range(5):
        for init in led[:4]:
            GPIO.output(init, 1)
        sleep(0.2)
        for init in led[:4]:
            GPIO.output(init, 0)
        sleep(0.2)


def main():
    continua = True
    andata()
    while(continua):
        if not (GPIO.input(bottoni[1])):
            ritorno()
            if not (GPIO.input(bottoni[0])):
                andata()
                vel -= 0.05
            else:
                vittoriaRosso()
                continua = False
        else:
            vittoriaVerde()
            continua = False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()

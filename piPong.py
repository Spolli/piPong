import RPi.GPIO as GPIO
from time import sleep
import sys

led = [3, 4, 17, 27, 22, 10, 9, 11]
bottoni = [2, 21]

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
    for i in reversed(led):
        GPIO.output(i, 1)
        sleep(0.2)
        GPIO.output(i, 0)
        sleep(0.2)

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
            else:
                vittoriaRosso()
                continua = False
        else:
            vittoriaVerde()
            continua = False

if __name__ == "__main__":
    main()

import RPi.GPIO as GPIO
from time import sleep
import random

led = [14, 15, 18, 23, 24, 25, 8, 7, 12]        #Numero dei pin a cui sono assegnati i led
bottoni = [2, 21]                               #Numero dei pin a cui sono assegnato i bottoni
controllo = [10 , 5]                            #Numero dei pin a cui sono asseganti per il controllo del primo e dell'ultimo led

def init():                                     #Inizializzo i led in output e i bottoni in input
    GPIO.setmode(GPIO.BCM)
    for i in led:
        GPIO.setup(i, GPIO.OUT)
    for i in bottoni:
        GPIO.setup(i, GPIO.IN)
    for i in controllo:
        GPIO.setup(i, GPIO.IN)
    GPIO.setwarnings(False)

def andata(vel):
    for i in led:
        GPIO.output(i, 1)
        sleep(vel)
        GPIO.output(i, 0)
        sleep(vel)

def ritorno(vel):
    for i in reversed(led):
        GPIO.output(i, 1)
        sleep(vel)
        GPIO.output(i, 0)
        sleep(vel)

def vittoriaPrimoGiocatore():                            #Funzione che segnala la vittoria del primo giocatore accendendo 5 volte i primi 6 led
    for time in range(5):
        for i in led[(len(led)/2):]:
            GPIO.output(i, 1)
        sleep(0.2)
        for i in led[(len(led)/2):]:
            GPIO.output(i, 0)
        sleep(0.2)

def vittoriaSecondoGiocatore():                            #Funzione che segnala la vittoria del secondo giocatore accendendo 5 volte gli ultimi 6 led
    for time in range(5):
        for i in led[:(len(led)/2)]:
            GPIO.output(i, 1)
        sleep(0.2)
        for i in led[:(len(led)/2)]:
            GPIO.output(i, 0)
        sleep(0.2)

def main():
    vel = 0.1                                               #velocità iniziale dei led
    continua = True
    andata(vel)
    while(continua):
        if (GPIO.input(bottoni[0]) == 0 && GPIO.input(controllo[0]) == 0):
            ritorno(vel)
	        vel = random.uniform(0.01, 0.1)                   #A ogni giro la velocità viene gerata randomicamente tra 0.01 secondi e 0.1 sec
            if (GPIO.input(bottoni[1]) == 0 && GPIO.input(controllo[1]) == 0):
                andata(vel)
		        vel = random.uniform(0.01, 0.1)
            else:
                vittoriaPrimoGiocatore()
                continua = False
        else:
            vittoriaSecondoGiocatore()
            continua = False

if __name__ == "__main__":
    init()
    try:
	       main()
    except KeyInterrupt:
	       GPIO.cleanup()

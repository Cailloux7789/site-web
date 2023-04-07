import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)

LedR = 18
LedV = 23
BP = 25

GPIO.setup (LedR, GPIO.OUT)
GPIO.setup (LedV, GPIO.OUT)
GPIO.setup (BP, GPIO.IN)

def cligno_dephase(pinA, pinB, Nb_cligno, tempo1, tempo2):
    for i in range(Nb_cligno):
        print("Oh sa clignote")
        GPIO.output(pinA, GPIO.HIGH)
        GPIO.output(pinB, GPIO.LOW)
        time.sleep(tempo1)
        GPIO.output(pinB, GPIO.HIGH)
        GPIO.output(pinA, GPIO.LOW)
        time.sleep(tempo2)

def cligno_phase(Nb_cligno, tempo1, tempo2):
    for i in range(Nb_cligno):
        print("Oh, toi aussi tu t allume")
        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.HIGH)
        time.sleep(tempo1)
        GPIO.output(LedR, GPIO.LOW)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(tempo2)

def ideeNathan(Nb_cligno):
    tempo1 = 1
    tempo2 = 1
    for i in range(Nb_cligno):
        cligno_dephase(LedV, LedR, 2, tempo1, tempo2)
        tempo1 = tempo1/1.5
        tempo2 = tempo2/1.5
    cligno_phase(2, 0.2,0.2)

cligno_dephase(LedV, LedR, 2, 1, 0.2)
while True:
    etat = GPIO.input(BP)
    if(etat == 1):
        print("OH SHIT HERE WE GO AGAIN")
        ideeNathan(15)
        print("Oh non c fini")
    elif(etat == 0):
        print("APPUIE SUR LE BOUTON")
        time.sleep(0.2)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LedR = 18
LedV = 23
BP = 25

GPIO.setup(LedR, GPIO.OUT)
GPIO.setup(LedV, GPIO.OUT)
GPIO.setup(BP, GPIO.IN)

def cligno_dephase(Nb_cligno, tempo1, tempo2):
    for i in range(Nb_cligno):
        print("En dephassage")

        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(tempo1)

        GPIO.output(LedV, GPIO.HIGH)
        GPIO.output(LedR, GPIO.LOW)
        time.sleep(tempo2)

def cligno_phase(Nb_cligno, tempo1, tempo2):
    for i in range(Nb_cligno):
        print("en phase")
        
        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.HIGH)
        time.sleep(tempo1)

        GPIO.output(LedR, GPIO.LOW)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(tempo2)

while True:

    etat = GPIO.input(BP)

    if(etat == 1):
        cligno_dephase(1, 0.5, 0.5)

    elif(etat == 0):
        cligno_phase(1, 0.5, 0.5)
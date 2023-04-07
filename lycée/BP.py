import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN)

while True:
    etat = GPIO.INPUT(25)

    if(etat == 1):
        print("bouton appuye")
    else:
        print("bouton relache")
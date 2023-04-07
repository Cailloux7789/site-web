import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

inter = 21
BP = 25
PIR = 23
buzzer = 18

GPIO.setup(inter, GPIO.IN)
GPIO.setup(BP, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

def Mode_manuel():
    etatBP = GPIO.input(BP)
    if(etatBP == 0):
        print("Bouton relache")
        GPIO.output(buzzer, GPIO.LOW)
    else:
        print("Bouton apuye")
        GPIO.output(buzzer, GPIO.HIGH)

def Mode_auto():
    etatPIR = GPIO.input(PIR)
    if(etatPIR == 0):
        print("PIR no detection")
        GPIO.output(buzzer, GPIO.HIGH)
    else:
        print("PIR detection")
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(0.5)

while True:
    etatinter = GPIO.input(inter)
    if(etatinter == 0):
        print("Mode manuel")
        Mode_manuel()
    else:
        print("Mode auto")
        Mode_auto()
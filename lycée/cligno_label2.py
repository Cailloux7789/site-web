import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)

LedR = 18
LedV = 23

GPIO.setup (LedR, GPIO.OUT)
GPIO.setup (LedV, GPIO.OUT)

while True:
    count1 = 0
    while (count1<7):
        print("en dephasage")
        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LedV, GPIO.HIGH)
        GPIO.output(LedR, GPIO.LOW)
        time.sleep(1)
        count1 = count1+1
    count2 = 0
    while (count2<4):
        print("en phase")
        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.HIGH)
        time.sleep(0.8)
        GPIO.output(LedR, GPIO.LOW)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(1.5)
        count2 = count2+1

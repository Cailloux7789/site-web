import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

while True:

    count1 = 0
    while(count1 < 7):
        print("En dephassage")

        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(23, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)

        count1 += 1

    count2 = 0
    while(count2 < 4):
        print("en phase")
        
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.8)

        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        time.sleep(1.5)

        count2 += 1
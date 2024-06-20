import RPi.GPIO as GPIO
import time

ledR = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)

try:
    while True:

        getKey = input('O(on)/X(off) >>>>  ')

        if getKey == 'o':
            GPIO.output(ledR, False)
        if getKey == 'x':
            GPIO.output(ledR, True)
except KeyboardInterrupt:
    GPIO.cleanup()



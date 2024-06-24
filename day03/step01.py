import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
    GPIO.setup(stepPin, GPIO.OUT)
    GPIO.output(stepPin, 0)

seq = [[0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 1, 0, 0],
       [1, 0, 0, 0]]

try:
    while True:
        for step in seq:
            for pin in range(len(steps)):
                GPIO.output(steps[pin], step[pin])
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()

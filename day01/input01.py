import RPi.GPIO as GPIO
import time

switch = 6
ledR = 21
ledB = 20
ledG = 26

index = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)



try:
	while True:
		if GPIO.input(switch) == True:

			if index == 0:
				GPIO.output(ledR, False)
				GPIO.output(ledB, True)
				GPIO.output(ledG, True)
				index += 1

			if index == 1:
				GPIO.output(ledR, True)
				GPIO.output(ledB, False)
				GPIO.output(ledG, True)
				index += 1

			if index == 2:
				GPIO.output(ledR, True)
				GPIO.output(ledB, True)
				GPIO.output(ledG, False)
				index = 0

except KeyboardInterrupt:
	GPIO.cleanup()

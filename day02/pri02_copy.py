import RPi.GPIO as GPIO
import time

pirPin = 24
ledR = 21
ledB = 20
ledG = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
			GPIO.output(ledR, False)
			print("감지됨")

		else:
			GPIO.output(ledR, True)

		time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()

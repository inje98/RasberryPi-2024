import RPi.GPIO as GPIO
import time

ledR = 21
#ledB = 20
#ledG = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledR, GPIO.OUT)
#GPIO.setup(ledB, GPIO.OUT)
#GPIO.setup(ledG, GPIO.OUT)

try:
	while True:
		GPIO.output(ledR, False)
#		GPIO.output(ledB, True)
#		GPIO.output(ledG, True)
		time.sleep(0.3)

except KeyboardInterrupt: #Ctrl + c
	GPIO.cleanup()

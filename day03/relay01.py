import RPi.GPIO as GPIO
import time

relayPin = 16 # 릴레이 S핀
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
	while True:

		GPIO.output(relayPin, 1)
		time.sleep(1)
		GPIO.output(relayPin, 0)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

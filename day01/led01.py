import RPi.GPIO as GPIO
import time

led1 = 21
led2 = 20
led3 = 26
#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/출력)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

try:
	while True:
		GPIO.output(led1, False)
		GPIO.output(led2, True)
		GPIO.output(led3, True)
		time.sleep(0.3)

		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, True)
		time.sleep(0.3)

		GPIO.output(led1, True)
		GPIO.output(led2, False)
		GPIO.output(led3, True)
		time.sleep(0.3)

		GPIO.output(led1, True)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		time.sleep(0.3)

		GPIO.output(led1, True)
		GPIO.output(led2, True)
		GPIO.output(led3, False)
		time.sleep(0.3)

		GPIO.output(led1, False)
		GPIO.output(led2, True)
		GPIO.output(led3, False)
		time.sleep(0.3)

		GPIO.output(led1, False)
		GPIO.output(led2, False)
		GPIO.output(led3, False)
		time.sleep(0.3)

except KeyboardInterrupt: #Ctrl + c
	GPIO.cleanup()

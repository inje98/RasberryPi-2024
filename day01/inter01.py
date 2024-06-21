# interrupt

import RPi.GPIO as GPIO
import time

# 핀설정
ledR = 21
switch = 6

# 인터럽트 변수
intFlag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

def ledBlink(channel):
	global intFlag
	if intFlag == False:
		GPIO.output(led,True)
		intFlag = True
	else:
		GPIO.output(led, False)
		intFlag = False

# 인터럽트 설정(switch핀에 rising 신호가 잡히면 callback함수를 실행)
GPIO.add_event_detect(switch, GPIO.RISING, callback=ledBlink)

try:
	while True:
		pass
except KeyboardTnterrupt:
	GPIO.cleanup()
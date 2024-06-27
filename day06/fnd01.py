# 강사님 답안
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 20, 16, 26, 19, 12, 13]
fndSels = [23, 24, 25, 4]

#GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data):
	for i in range(0, 7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))

try:
	while True:
		for i in range(0, 1):
			GPIO.output(fndSels[i], 0)		# fnd 선택

#			GPIO.output(20, 1)
#			GPIO.output(16, 1)

			for j in range(0, 10):
				fndOut()
				time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()

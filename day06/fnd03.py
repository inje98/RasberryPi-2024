# 강사님 답안
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 20, 16, 26, 19, 12, 13]
fndSels = [4, 25, 24, 23]
#fndSels = [23, 24, 25, 4]
count = 0

#GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data, sel):
	for i in range(0, 7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
		for j in range(0, 4): # 자리수의 fnd만 on
			if j == sel:
				GPIO.output(fndSels[j], 0)
			else:
				GPIO.output(fndSels[j], 1)

try:
	while True:
		count += 1
		d1000 = count / 1000
		d100 = count %1000 / 100
		d10 = count % 100 / 10
		d1 = count % 10
		d = [d1, d10, d100, d1000]

		for i in range(3, -1, -1):
			fndOut(int(d[i]), i)				# 자리수와 값을 전달
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()

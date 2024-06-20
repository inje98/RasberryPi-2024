import RPi.GPIO as GPIO
import time

piezoPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)
Buzz.start(1)  # PWM 시작, 초기 듀티 사이클을 50%로 설정

try:
    while True:
    	
        getKey = int(input('>>> '))
        if getKey == 1:
            Buzz.ChangeFrequency(130)
        elif getKey == 2:
            Buzz.ChangeFrequency(147)
        elif getKey == 3:
            Buzz.ChangeFrequency(165)
        elif getKey == 4:
            Buzz.ChangeFrequency(175)
        elif getKey == 5:
            Buzz.ChangeFrequency(196)
        elif getKey == 6:
            Buzz.ChangeFrequency(220)
        elif getKey == 7:
            Buzz.ChangeFrequency(247)
        elif getKey == 8:
            Buzz.ChangeFrequency(262)
		
        time.sleep(0.1)  # 소리가 약 0.1초 동안 지속되게 대기
        Buzz.ChangeFrequency(1)  # 소리를 멈춥니다.
        time.sleep(0.1)
		  


except KeyboardInterrupt:
    Buzz.stop()  # PWM 종료
    GPIO.cleanup()  # GPIO 리소스 정리

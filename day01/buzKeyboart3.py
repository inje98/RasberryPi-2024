import RPi.GPIO as GPIO
import time

piezoPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)
Buzz.start(0)  # 초기 PWM 시작 시 듀티 사이클을 0%로 설정

try:
    while True:
        getKey = int(input('Enter a number (1-8) to change frequency: '))
        
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
        
        Buzz.ChangeDutyCycle(10)  # 듀티 사이클을 낮춰서 소리를 작게 설정 (예: 10%)
        time.sleep(0.1)  # 소리가 약 0.1초 동안 지속되게 대기
        Buzz.ChangeDutyCycle(0)  # 듀티 사이클을 0%로 설정하여 소리 멈춤
        time.sleep(0.1)  # 다음 입력을 위해 약간의 딜레이를 추가

except KeyboardInterrupt:
    Buzz.stop()  # PWM 종료
    GPIO.cleanup()  # GPIO 리소스 정리

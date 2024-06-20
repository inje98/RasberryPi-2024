import RPi.GPIO as GPIO
import time

switch = 6
ledR = 21
ledB = 20
ledG = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)

index = 0
last_state = GPIO.input(switch)  # 풀다운이니까 처음 Low

try:
    while True:
        current_state = GPIO.input(switch) # 누를때 High
        if last_state == GPIO.LOW and current_state == GPIO.HIGH:  # 스위치가 눌렸을 때
            if index == 0:
                GPIO.output(ledR, False)
                GPIO.output(ledB, True)
                GPIO.output(ledG, True)
                index = 1
            elif index == 1:
                GPIO.output(ledR, True)
                GPIO.output(ledB, False)
                GPIO.output(ledG, True)
                index = 2
            elif index == 2:
                GPIO.output(ledR, True)
                GPIO.output(ledB, True)
                GPIO.output(ledG, False)
                index = 0

        last_state = current_state
        # 꾹 누르고 있거나 안누르고 있으면 변화 없다가
        # 딱 누를때만 (last==low, cur==high)일때만
        # index 1올라가면서 색 바뀌는거지
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

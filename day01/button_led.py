import RPi.GPIO as GPIO
import time

switch = 6
ledR = 21
ledB = 20
ledG = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 풀업 저항을 사용하여 입력 핀을 플로팅 상태로 만들지 않습니다.
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)

# RGB LED의 색상 상태를 저장하기 위한 리스트
colors = [
    (True, False, False),  # Red
    (False, True, False),  # Green
    (False, False, True),  # Blue
]

color_index = 0  # 현재 색상 인덱스
last_state = GPIO.input(switch)  # 마지막 스위치 상태

try:
    while True:
        current_state = GPIO.input(switch)
        if last_state == GPIO.HIGH and current_state == GPIO.LOW:  # 스위치가 눌렸을 때
            color_index = (color_index + 1) % len(colors)  # 다음 색상으로 변경
            print(f"스위치 눌림 - 색상: {colors[color_index]}")
            GPIO.output(ledR, colors[color_index][0])
            GPIO.output(ledB, colors[color_index][1])
            GPIO.output(ledG, colors[color_index][2])

        last_state = current_state  # 마지막 상태 업데이트
        time.sleep(0.1)  # 작은 딜레이 추가
except KeyboardInterrupt:
    GPIO.cleanup()

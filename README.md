# RasberryPi-2024
라즈베리파이

## 1일차
- GPIO 설정함수
    - GPIO.setmode(GPIO.BOARD) - wPi
    - GPIO.setmode(GPIO.BCM) - BCM
    - GPIO.setup(channel, GPIO.mode)
        - channel: 핀번호, mode: IN/OUT
    -GPIO.cleanup()
- GPIO 출력함수
    - GPIO.output(channel, state)
        - channel: 핀번호, state: HIGH/LOW or 1/0 or True/False

- GPIO 입력함수
    - GPIO.input(channel)
        - channel: 핀번호, 반환값: H/L or 1/0 or T/F

- 시간지연 함수
    - time.sleep(sec)

- button
    - 풀업 버튼
        ![PullUp](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/PullUp.png)
    - 풀다운 버튼
        ![PullDown](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/PullDown.png)

- buzzor
    - Buzz = GPIO.PWM(piezoPin, 440) -> 아날로그 출력을 위한 객체생성(440Hz 출력)  
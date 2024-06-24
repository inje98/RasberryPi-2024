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
    - 입력핀에 5v나 0v가 읽히게됨

    - 풀업 버튼
        ![PullUp](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/PullUp.png)

        - 평상시 접지부분이 오픈되어 있으믈 입력핀에 5v가 읽힌다
        - 버튼이 눌리면 입력핀 0v가 읽힌다


    - 풀다운 버튼
        ![PullDown](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/PullDown.png)

        - 평상시 전원으로부터 끊어져있으므로 입력핀에 0v가 읽힌다
        - 버튼이 눌리면 접지 부분에 저항이 있으므로 입력핀에 5v가 읽힌다

- buzzor
    - Buzz = GPIO.PWM(piezoPin, 440) -> 아날로그 출력을 위한 객체생성(440Hz 출력)

## 2일차
- 가상환경
    1. python -m venv env --> env 가상환경을 생성
    1-1.  python -m venv --system-site-packages env --> 모든 pip 깔린채로 가상환경 쓰는거인듯
    2. source ./env/bin/activate  --> env 가상환경에 입장
    3. deactivate --> 가상환경 나오기

- 라즈베리파이 현재 상태보기
    1. sudo git clone https://gitbub.com/WiringPi/WiringPi  --> WiringPi 생성
    2. cd WiringPi 들어가서
    3. sudo ./build --> 뭐가 쭉 깔림
    4. gpio readall --> 현재 라즈베리파이 상황을 볼 수 있다. 어디에 현재 전압이 걸려있고 그런것들

- 동작감지 센서
- 초음파 센서
``` python
    GPIO.output(trigPin, True)
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()
    # 위 코드가 초음파를 10us동안 뾱 보낸거임
     
```
``` python
    GPIO.input(echoPin) == True
    #보낸 초음파가 echoPin으로 들어오면 True가 되고, 초음파가 갔다온 시간을 계산해서 반환하는 함수를 만들어서, 그 값으로 무언가를 제어
```
    
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

## 3일차
- 릴레이
    - 릴레이는 안에 있는 코일 -> 코일에 전류가 흐르면 자기장 발생 -> 자기장으로 인해 전자석이 됨 -> 이 전자석으로 인해 회로를 끊었다 붙였다하며 스위치 역할을 함
![relay](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/relay.jpg)
- 오른편 제어할 회로를 구성
    - NO : Normal Open -> 평상시 오픈, 릴레이 동작시 연결
    - NC : Normal Close -> 평상시 연결, 릴레이 동작시 오픈
    - COM : 전원선 연결
- 왼편 라즈베리파이/아두이노 회로 구성
    - 늘 그렇듯 시그널 핀, 5V, GND 연결
    - 이쪽편에서 5v를 줬다 뺐다 하면서 LED를 제어하는것

- 스탭모터
    - 스탭모터는 360도 회전이 되고 32개의 톱니바퀴가 4개의 전자석을 통해 한번에 한단계씩 회전시키는 방식으로 작동한다
![Motor](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/Motor.png)

- 입력핀 4개가 각각 하나의 전자석에 신호 줌으로써 모터를 제어한다.
``` python
        GPIO.output(steps[0], 0)
        GPIO.output(steps[1], 0)
        GPIO.output(steps[2], 0)
        GPIO.output(steps[3], 1)
        time.sleep(0.01)

        GPIO.output(steps[0], 0)
        GPIO.output(steps[1], 0)
        GPIO.output(steps[2], 1)
        GPIO.output(steps[3], 0)
        time.sleep(0.01)

        GPIO.output(steps[0], 0)
        GPIO.output(steps[1], 1)
        GPIO.output(steps[2], 0)
        GPIO.output(steps[3], 0)
        time.sleep(0.01)

        GPIO.output(steps[0], 1)
        GPIO.output(steps[1], 0)
        GPIO.output(steps[2], 0)
        GPIO.output(steps[3], 0)
```
    - 다음과 같이 계속해서 한쪽 방향으로 모터를 돌릴 수 있다.

- 라즈베리파이 서버(flask)
    ```python
        from flask import Flask

        app = Flask(__name__) 

        @app.route("/")
        def hello():
	        return "Hello World!"

        if __name__ == "__main__":
	        app.run(host="0.0.0.0", port="10110", debug=True) 
    ```
    - 기본적인 웹 코드
    - 웹에 라즈베리파이 ip와 포트번호를 쳐서 들어간다

    ```python
        @app.route("/led/on")
        def on():
	        GPIO.output(ledR, False)
	        return "<h1>led on</h1>"

        @app.route("/led/off")
        def off():
	        GPIO.output(ledR, True)
	        return "<h1>led off</h1>"
    ```
    - 이런식으로 웹을 통해서 LED 켜고끄고 제어가 가능하다.
    - 실제 버튼을 누르면 웹에 어떤 이벤트가 발생한다던지, 웹을 통해서 다양한 부품들을 동작 시키는 등 다양하게 서버를 활용해서 많은것을 해볼 수 있을 것 같다.

    ``` python
        from flask import Flask, request

        app = Flask(__name__)

        @app.route("/")
        def get():
            value1 = request.args.get("이름", "user")
            value2 = request.args.get("주소", "부산")
            return value1 + ":" + value2

        if __name__ == "__main__":
	        app.run(host="0.0.0.0", port="10011", debug=True)
    ```
- request.args에 있는 get함수를 이용해서 키(이름) 값(user) 형태로 입력 받을 수 있다
- 192.168.5.3:10011/ 이렇게 들어가면 user:부산 이 화면에 뜬다. user, 부산을 디폴트로 넣어놨으니까
- 키에 값을 넣는 방법
    - 192.168.5.3:10011/?이름=김인제&주소=대구
    - 이런식으로 넣는다.
    - 만약 192.168.5.3:10011/?이름=김인제 까지 적으면 주소는 디폴트로 설정한 부산이 나온다.

## 4일차
- html을 작성하고 그 화면에서 led제어하기
    - flask 모듈안의 render_template()함수를 이용해 만들어둔 html파일의 내용을 불러와 리턴 시키도록 만든다.
    - 버튼을 누르면 data변수에 on이나 off가 들어가도록 하고 둘을 if문으로 구별시켜서 led제어

- 카메라
    - 카메라 사용법
    - 버튼을 누르면 카메라 동작

- 7세그먼트
    ![7seg](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/7segment%EA%B5%AC%EC%A1%B0.png)

    - com1, com2, com3, com4 각각 첫번째, 두번째, 세번째, 네번째 칸을 담당
    - 위에 보이는 a~g까지의 핀과 com핀에 전압을 걸어서 번호를 표현하면서 제어 할 수 있다.

    ![7segment](https://raw.githubusercontent.com/inje98/RasberryPi-2024/main/image/7%EC%84%B8%EA%B7%B8%EA%B5%AC%EC%A1%B0.png)

## 5일차

- 7세그먼트
    1. 특정 숫자에 해당하는 핀에 5v신호를 주고 com1핀(첫번째칸)을 순간적으로 0v를 줬다 뺀다.
    2. 다음 칸에 그릴 숫자에 해당하는 핀에 5v를 주고 다음 com핀을 줬다 뺀다.
    3. 이걸 엄청나게 빠르게 반복해서 화면에 띄우는거임.
    4. 얼핏 보기엔 계속 화면에 숫자가 띄어져 있는것처럼 보이나 실제론 엄청나게 빠르게 com1, com2, com3, com4핀과 숫자핀이 깜빡깜빡 거리고 있는거다.

    - FND로 해본것들
        - 일단 1234 띄어보기
        - 버튼 누르면 카운트되게 만들어보기
        - 초음파센서로 값을 받고 그 값을 FND화면에 띄어보기

## 6일차
- 7세그먼트
    - 어제 해본거 강사님의 코드
        - 새로 안 스킬
            - 당연히 전체적인 매커니즘은 똑같지만 비트연산 스킬을 배웠다.
            ``` python
                for i in range(0, 7):
			        GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
            ```
            - fndDatas에 16진수 비트를 배열로 만들어 놓고, 비트곱연산과 비트시프트 연산을 통해 fndSegs 요소에 해당 비트를 각각 넣어주는 스킬
            - 저렇게 원하는 숫자핀에 전압을 넣고 com1,2,3,4에 번갈아가며 0v를 주는 식으로 코드를 짰다.

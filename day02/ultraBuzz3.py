import RPi.GPIO as GPIO
import time

def measure():
    GPIO.output(trigPin, True)  # 10us 동안 high레벨로 triger출력하여 초음파 발생 준비
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    start = time.time()  # 현재시간 저장

    while GPIO.input(echoPin) == False:  # echo가 없으면
        start = time.time()  # 현재 시간을 start변수에 저장하고
    while GPIO.input(echoPin) == True:  # echo가 있으면
        stop = time.time()  # 현재시간을 stop변수에 저장
    elapsed = stop - start  # 걸린 시간을 구하고
    distance = (elapsed * 34300) / 2  # 초음파 속도를 이용해서 거리계산

    return distance

# 핀설정
trigPin = 23
echoPin = 24
piezoPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)
# Buzz.start(50)

try:
    while True:
        distance = measure()
        print("Distance: %.2f cm" % distance)
        Buzz.start(30)
        if distance < 5:
            Buzz.ChangeFrequency(1000)
            time.sleep(0.05)
        elif distance < 10:
            Buzz.ChangeFrequency(500)
            time.sleep(0.1)
        elif distance < 15:
            Buzz.ChangeFrequency(250)
            time.sleep(0.2)
        else:
            Buzz.stop()
        time.sleep(0.1)

except KeyboardInterrupt:
    Buzz.stop()
    GPIO.cleanup()

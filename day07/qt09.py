import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QTimer

GPIO.setmode(GPIO.BCM)
pin = (21, 20, 16, 26, 19, 12, 13)
digits = (23, 24, 25, 4)

number_list = {
    '0': (1, 1, 1, 1, 1, 1, 0),
    '1': (0, 1, 1, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1),
    '3': (1, 1, 1, 1, 0, 0, 1),
    '4': (0, 1, 1, 0, 0, 1, 1),
    '5': (1, 0, 1, 1, 0, 1, 1),
    '6': (1, 0, 1, 1, 1, 1, 1),
    '7': (1, 1, 1, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1)
}

Mag = 22
trigPin = 18
echoPin = 17
ledR = 5
ledB = 6
ledG = 27

GPIO.setup(Mag, GPIO.IN)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)

for a in pin:
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.LOW)

for b in digits:
    GPIO.setup(b, GPIO.OUT)
    GPIO.output(b, GPIO.HIGH)
# 여기까지가 핀 번호 설정, 셋팅


def measure(): # 초음파 측정 함수, 거리를 cm로 계산해서 반환
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    start = time.time()
    while GPIO.input(echoPin) == GPIO.LOW:
        start = time.time()
    
    while GPIO.input(echoPin) == GPIO.HIGH:
        stop = time.time()
    
    elapsed = stop - start
    distance = (elapsed * 19000) / 2
    return distance

def split_num(number):
    num = [int(i) for i in str(number).zfill(4)]
    return num
# 인자로 number를 받아서 4자리로 쪼개서 리스트로 반환
# index1,2,3,4 에다가 각각 넣어줄거

def displayNum(index):
    for i in range(7):
        GPIO.output(pin[i], number_list[index][i])

form_class = uic.loadUiType("./project01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.index1 = 0
        self.index2 = 0
        self.index3 = 0
        self.index4 = 0
        self.count = 0

        self.btnUltra.clicked.connect(self.UltraStart)
        self.btnCount.clicked.connect(self.CountStart)
        self.btnLED.clicked.connect(self.LEDStart)
        self.btnOn.clicked.connect(self.LED_On)
        self.btnOff.clicked.connect(self.LED_Off)
        self.btnPlus.clicked.connect(self.Plus1)
        self.btnMag.clicked.connect(self.MagStart)
        self.btnMagOff.clicked.connect(self.MagClose)

	# QTimer 객체 생성
	# 시간을 재서 몇초마다 어떤 함수를 호출하겠다
	# while 대신에 이렇게 쓸거임
        self.timer = QTimer()
        self.timerCount = QTimer()
        self.timerMag = QTimer()


    def Mag(self):
        if (GPIO.input(Mag) == True):
            self.MagLabel.setText("떨어졌다")
        elif (GPIO.input(Mag) == False):
            self.MagLabel.setText("붙었다")


    def MagStart(self): # 마그네틱 시작 버튼
        #self.btnMagOff.setEnabled(True)
        self.MagLabel.show()
        self.timerMag.timeout.connect(self.Mag) # 1초마다(1000) Mag함수 호출
        self.timerMag.start(1000)
    
    def MagClose(self): # 마그네틱 off버튼
        #self.btnMagOff.setEnabled(False)
        self.timerMag.stop()
        self.MagLabel.hide()

    def UltraStart(self): # 초음파 시작 버튼
        self.label.show()
        self.label.setText("cm")

        GPIO.output(ledR, True)
        GPIO.output(ledB, True)
        GPIO.output(ledG, True)

        self.btnOn.setEnabled(False)
        self.btnOff.setEnabled(False)
        self.btnPlus.setEnabled(False)

        self.timer.timeout.connect(self.updateDistance)
        self.timer.start(3000)

    def updateDistance(self): # 3초마다 이 함수 호출
        distance = measure()
        self.lcdNumber.display(int(distance))
        DistanceAry = split_num(int(distance))

        self.index1 = DistanceAry[0]
        self.index2 = DistanceAry[1]
        self.index3 = DistanceAry[2]
        self.index4 = DistanceAry[3]

        for _ in range(50):  
            displayNum(str(self.index1))
            GPIO.output(digits[0], 0)
            time.sleep(0.005)
            GPIO.output(digits[0], 1)

            displayNum(str(self.index2))
            GPIO.output(digits[1], 0)
            time.sleep(0.005)
            GPIO.output(digits[1], 1)

            displayNum(str(self.index3))
            GPIO.output(digits[2], 0)
            time.sleep(0.005)
            GPIO.output(digits[2], 1)

            displayNum(str(self.index4))
            GPIO.output(digits[3], 0)
            time.sleep(0.005)
            GPIO.output(digits[3], 1)

    def CountStart(self): # 카운트 시작 버튼
        self.count = 0
        self.index4 = 0
        self.index3 = 0
        self.index2 = 0
        self.index1 = 0
        self.lcdNumber.display(0)

        self.label.show()
        self.label.setText("회")

        GPIO.output(ledR, True)
        GPIO.output(ledB, True)
        GPIO.output(ledG, True)

        self.btnOn.setEnabled(False)
        self.btnOff.setEnabled(False)
        self.btnPlus.setEnabled(True)

        self.timer.stop()
        self.timerCount.stop()
        
        self.lcdNumber.display(self.count)

        self.timerCount.timeout.connect(self.FNDShow)
        self.timerCount.start(1)
        #self.timerCount.stop()


    def FNDShow(self): # index1,2,3,4 각각 다 숫자모양 만들고, com1,2,3,4 0v 줬다뺐다 반복
        displayNum(str(self.index1))
        GPIO.output(digits[0], 0)
        time.sleep(0.001)
        GPIO.output(digits[0], 1)

        displayNum(str(self.index2))
        GPIO.output(digits[1], 0)
        time.sleep(0.001)
        GPIO.output(digits[1], 1)

        displayNum(str(self.index3))
        GPIO.output(digits[2], 0)
        time.sleep(0.001)
        GPIO.output(digits[2], 1)

        displayNum(str(self.index4))
        GPIO.output(digits[3], 0)
        time.sleep(0.001)
        GPIO.output(digits[3], 1)

        

    def Plus1(self):
        self.index4 += 1
        self.count += 1

        if self.index4 == 10:
            self.index3 += 1
            self.index4 = 0
        if self.index3 == 10:
            self.index2 += 1
            self.index3 = 0
        if self.index2 == 10:
            self.index1 += 1
            self.index2 = 0
        if self.index1 == 10:
            self.index1 = 0

        self.lcdNumber.display(self.count)

    def LEDStart(self): #LED 시작 버튼
        self.btnOn.setEnabled(True)
        self.btnOff.setEnabled(True)
        self.btnPlus.setEnabled(False)

        self.label.hide()

        self.timer.stop()
        self.timerCount.stop()
        self.count = 0
        self.index4 = 0
        self.index3 = 0
        self.index2 = 0
        self.index1 = 0

        self.lcdNumber.display(0)

    def LED_On(self):
        if self.radioRed.isChecked():
            GPIO.output(5, False)
            GPIO.output(6, True)
            GPIO.output(27, True)
        elif self.radioBlue.isChecked():
            GPIO.output(5, True)
            GPIO.output(6, False)
            GPIO.output(27, True)
        elif self.radioGreen.isChecked():
            GPIO.output(5, True)
            GPIO.output(6, True)
            GPIO.output(27, False)
    
    def LED_Off(self):
         GPIO.output(5, True)
         GPIO.output(6, True)
         GPIO.output(27, True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    GPIO.cleanup()

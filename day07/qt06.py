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
    '0': (1, 1, 1, 1, 1, 1, 0),  # 0
    '1': (0, 1, 1, 0, 0, 0, 0),  # 1
    '2': (1, 1, 0, 1, 1, 0, 1),  # 2
    '3': (1, 1, 1, 1, 0, 0, 1),  # 3
    '4': (0, 1, 1, 0, 0, 1, 1),  # 4
    '5': (1, 0, 1, 1, 0, 1, 1),  # 5
    '6': (1, 0, 1, 1, 1, 1, 1),  # 6
    '7': (1, 1, 1, 0, 0, 0, 0),  # 7
    '8': (1, 1, 1, 1, 1, 1, 1),  # 8
    '9': (1, 1, 1, 1, 0, 1, 1)   # 9
}

index1 = 0
index2 = 0
index3 = 0
index4 = 0

trigPin = 18
echoPin = 17
ledR = 5
ledB = 6
ledG = 27

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

index1 = 0 # 첫째자리
index2 = 0 # 둘째자리
index3 = 0 # 셋째자리
index4 = 0 # 넷째자리


def measure(): # 초음파 쏴서 거리 반환하는 함수
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    start = time.time()
    while GPIO.input(echoPin) == GPIO.LOW:
        start = time.time()
    
    while GPIO.input(echoPin) == GPIO.HIGH:
        stop = time.time()
    
    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    return distance

def split_num(number):
    num = [int(i) for i in str(number).zfill(4)]
    return num

def displayNum(index):
    for i in range(7):
        GPIO.output(pin[i], number_list[index][i])


form_class = uic.loadUiType("./project01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnUltra.clicked.connect(self.UltraStart)
        self.btnCount.clicked.connect(self.CountStart)
        self.btnLED.clicked.connect(self.LEDStart)
        self.btnOn.clicked.connect(self.LED_On)
        self.btnOff.clicked.connect(self.LED_Off)
        self.btnCleanup.clicked.connect(self.Clean)
        self.btnPlus.clicked.connect(self.Plus1)

        

        self.timer = QTimer()

        # self.radioRed.toggled.connect(self.radioClick)
        # self.radioBlue.toggled.connect(self.radioClick)
        # self.radioGreen.toggled.connect(self.radioClick)
    

    def Clean(self): # 뭔가 팅기듯이 나가짐
        GPIO.cleanup()

# -------------- 초음파 -------------------
    def UltraStart(self): # 3초마다 updataDistance 호출하는 함수
        GPIO.output(ledR, True)
        GPIO.output(ledB, True)
        GPIO.output(ledG, True)

        self.btnOn.setEnabled(False)
        self.btnOff.setEnabled(False)
        self.btnPlus.setEnabled(False)

        
        self.timer.timeout.connect(self.updateDistance)
        self.timer.start(3000)   # 3초마다 updateDistance함수 호출
                                 # 이거 짧게하니까 렉 너무 걸린다
        
        

    def updateDistance(self): # 숫자 화면에 띄우고  FND에 띄우고
        distance = measure()
        self.lcdNumber.display(int(distance))
        DistanceAry = split_num(int(distance))

        index1 = DistanceAry[0]
        index2 = DistanceAry[1]
        index3 = DistanceAry[2]
        index4 = DistanceAry[3]

        for _ in range(50):  
            displayNum(str(index1))
            GPIO.output(digits[0], 0)
            time.sleep(0.005)
            GPIO.output(digits[0], 1)

            displayNum(str(index2))
            GPIO.output(digits[1], 0)
            time.sleep(0.005)
            GPIO.output(digits[1], 1)

            displayNum(str(index3))
            GPIO.output(digits[2], 0)
            time.sleep(0.005)
            GPIO.output(digits[2], 1)

            displayNum(str(index4))
            GPIO.output(digits[3], 0)
            time.sleep(0.005)
            GPIO.output(digits[3], 1)
# -------------- 초음파 -------------------

# -------------- 카운트 -------------------
    def CountStart(self):
        #print("Count Button Clicked")
        GPIO.output(ledR, True)
        GPIO.output(ledB, True)
        GPIO.output(ledG, True)

        self.btnOn.setEnabled(False)
        self.btnOff.setEnabled(False)
        self.btnPlus.setEnabled(True)

        self.timer.stop()
        self.lcdNumber.display(0)

        displayNum(str(index1))
        GPIO.output(digits[0],0)
        time.sleep(0.001)
        GPIO.output(digits[0],1)

        displayNum(str(index2))
        GPIO.output(digits[1],0)
        time.sleep(0.001)
        GPIO.output(digits[1],1)

        displayNum(str(index3))
        GPIO.output(digits[2],0)
        time.sleep(0.001)
        GPIO.output(digits[2],1)

        displayNum(str(index4))
        GPIO.output(digits[3],0)
        time.sleep(0.001)
        GPIO.output(digits[3],1)

    count = 0
    def Plus1(self):
        index4 += 1
        count += 1
        self.lcdNumber.display(count)

# -------------- 카운트 -------------------- 


# --------------- LED --------------------
    # def radioClick(self):
    #     if self.radioRed.isChecked():
    #         print("Radio Button 1 selected")
    #     elif self.radioBlue.isChecked():
    #         print("Radio Button 2 selected")
    #     elif self.radioGreen.isChecked():
    #         print("Radio Button 3 selected")


    def LEDStart(self):
        #print("LED ON Button Clicked")
        self.btnOn.setEnabled(True)
        self.btnOff.setEnabled(True)
        self.btnPlus.setEnabled(False)

        self.timer.stop()
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

# --------------- LED --------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    GPIO.cleanup()

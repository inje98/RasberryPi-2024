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

def measure():
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
        self.btnCleanup.clicked.connect(self.Clean)
        self.btnPlus.clicked.connect(self.Plus1)
        self.btnMag.clicked.connect(self.MagStart)


        self.timer = QTimer()
        self.timerCount = QTimer()
        self.timerMag = QTimer()


    def Mag(self):
        if (GPIO.input(Mag) == True):
            self.MagLabel.setText("떨어졌다")
        elif (GPIO.input(Mag) == False):
            self.MagLabel.setText("붙었다")


    def Clean(self):
        GPIO.cleanup()

    def MagStart(self):
        self.timerMag.timeout.connect(self.Mag)
        self.timerMag.start(1000)

    def UltraStart(self):
        self.label.show()
        self.label.setText("cm")

        self.label_1.hide()
        self.label_2.hide()
        self.label_3.hide()


        GPIO.output(ledR, True)
        GPIO.output(ledB, True)
        GPIO.output(ledG, True)

        self.btnOn.setEnabled(False)
        self.btnOff.setEnabled(False)
        self.btnPlus.setEnabled(False)

        self.timer.timeout.connect(self.updateDistance)
        self.timer.start(3000)

    def updateDistance(self):
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

    def CountStart(self):
        self.count = 0
        self.index4 = 0
        self.index3 = 0
        self.index2 = 0
        self.index1 = 0
        self.lcdNumber.display(0)

        self.label_1.hide()
        self.label_2.hide()
        self.label_3.hide()

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


    def FNDShow(self):
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

    def LEDStart(self):
        self.btnOn.setEnabled(True)
        self.btnOff.setEnabled(True)
        self.btnPlus.setEnabled(False)

        self.label_1.show()
        self.label_2.show()
        self.label_3.show()
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

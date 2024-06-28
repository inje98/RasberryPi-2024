import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 20, 16, 26, 19, 12, 13]
fndSels = [3, 24, 25, 4]
red = 26
blue = 19
green = 13

# GPIO ?ㅼ젙
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

for fndSeg in fndSegs:
    GPIO.setup(fndSeg, GPIO.OUT)
    GPIO.output(fndSeg, 0)

for fndSel in fndSels:
    GPIO.setup(fndSel, GPIO.OUT)
    GPIO.output(fndSel, 1)

# UI ?뚯씪 濡쒕뱶
form_class = uic.loadUiType("./testgui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # QTimer ?ㅼ젙
        self.fnd_timer = QTimer(self)
        self.fnd_timer.timeout.connect(self.updateFND)
        self.led_timer = QTimer(self)
        self.led_timer.timeout.connect(self.changeLED)
        self.led_state = 0  # 珥덇린 ?곹깭: Red LED

        # 踰꾪듉 ?대깽???곌껐
        self.btnstart.clicked.connect(self.startFND)
        self.btnstop.clicked.connect(self.stopFND)
        self.btn_on.clicked.connect(self.startLED)
        self.btn_off.clicked.connect(self.stopLED)
        self.btncleanup.clicked.connect(self.cleanup)

        # LCD 珥덇린??        self.lcdNumber.display(0)

        # FND 珥덇린??        self.count_fnd = 0
        self.fnd_running = False  # FND ?숈옉 ?щ?

    def startFND(self):
        if not self.fnd_running:
            self.fnd_running = True
            self.fnd_timer.start(1)  # 1ms 媛꾧꺽?쇰줈 FND ?낅뜲?댄듃

    def stopFND(self):
        self.fnd_running = False
        self.fnd_timer.stop()
#        self.clearFND()  # FND 珥덇린??
    def updateFND(self):
        if self.fnd_running:
            if self.count_fnd <= 9999:
                self.displayFND(self.count_fnd)
                self.displayLCD(self.count_fnd)
                self.count_fnd += 1
            else:
                self.stopFND()

    def displayFND(self, num):
        d1000 = num // 1000
        d100 = (num % 1000) // 100
        d10 = (num % 100) // 10
        d1 = num % 10
        
        for i, d in enumerate([d1, d10, d100, d1000]):
            fndOut(d, i)
            time.sleep(0.001)  # ?쒕젅???ㅼ젙
            #fndOut(0x00, i)  # FND 珥덇린??
 #   def clearFND(self):
  #      for i in range(4):
   #         fndOut(0x00, i)

    def startLED(self):
        self.led_timer.start(1000)

    def stopLED(self):
        self.led_timer.stop()
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(green, True)

    def changeLED(self):
        if self.led_state == 0:
            GPIO.output(red, False)
            GPIO.output(blue, True)
            GPIO.output(green, True)
            self.led_state = 1
        elif self.led_state == 1:
            GPIO.output(red, True)
            GPIO.output(blue, False)
            GPIO.output(green, True)
            self.led_state = 2
        elif self.led_state == 2:
            GPIO.output(red, True)
            GPIO.output(blue, True)
            GPIO.output(green, False)
            self.led_state = 0

    def displayLCD(self, num):
        self.lcdNumber.display(num)

    def cleanup(self):
        self.fnd_timer.stop()
        self.led_timer.stop()
        GPIO.cleanup()
        self.lcdNumber.display(0)
        self.count_fnd = 0
        for fndSeg in fndSegs:
            GPIO.setup(fndSeg, GPIO.OUT)
            GPIO.output(fndSeg, GPIO.LOW)
        for fndSel in fndSels:
            GPIO.setup(fndSel, GPIO.OUT)
            GPIO.output(fndSel, GPIO.HIGH)

    def closeEvent(self, event):
        self.cleanup()
        event.accept()

def fndOut(data, sel):
    for i in range(0, 7):
        GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
    
    for j in range(0, 4):
        if j == sel:
            GPIO.output(fndSels[j], GPIO.LOW)
        else:
            GPIO.output(fndSels[j], GPIO.HIGH)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())

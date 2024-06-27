import RPi.GPIO as GPIO
import time
import datetime

switch = 6
oldSw = 0
newSw = 0

a = 21
b = 20
c = 16
d = 26
e = 19
f = 12
g = 13

index = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

def one():
    GPIO.output(a, False)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, False)
    # [0,1,1,0,0,0,0]

def two():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, False)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, False)
    GPIO.output(g, True)
    # [1,1,0,1,1,0,1]
def three():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, True)
    # [1,1,1,1,0,0,1]
def four():
    GPIO.output(a, False)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)
    # [0,1,1,0,0,1,1]
def five():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)
    # [1,0,1,1,0,1,1]
def six():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)
    #[1,0,1,1,1,1,1]
def seven():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, False)
    #[1,1,1,0,0,1,0]
def eight():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)
    #[1,1,1,1,1,1,1]
def nine():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)
    # [1,1,1,1,0,1,1]
def zero():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, False)
    # [1,1,1,1,1,1,0]
try:
    while True:
        newSw = GPIO.input(switch)
        if newSw != oldSw:
            oldSw = newSw

            if newSw == 1:
                #print("click")
                if index == 1:
                    one()
                    index = 2
                #time.sleep(1)
                elif index == 2:
                    two()
                    index = 3
                #time.sleep(1)
                elif index == 3:
                    three()
                    index = 4
                #time.sleep(1)
                elif index == 4:
                    four()
                    index = 5
                #time.sleep(1)
                elif index == 5:
                    five()
                    index = 6
                #time.sleep(1)
                elif index == 6:
                    six()
                    index = 7
                #time.sleep(1)
                elif index == 7:
                    seven()
                    index = 8
                #time.sleep(1)
                elif index == 8:
                    eight()
                    index = 9
                #time.sleep(1)
                elif index == 9:
                    nine()
                    index = 0
                #time.sleep(1)
                elif index == 0:
                    zero()
                    index = 1
                #time.sleep(1)
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()

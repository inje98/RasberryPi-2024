import RPi.GPIO as GPIO
import time

a = 21
b = 20
c = 16
d = 26
e = 19
f = 12
g = 13

GPIO.setmode(GPIO.BCM)
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

def two():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, False)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, False)
    GPIO.output(g, True)

def three():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, True)

def four():
    GPIO.output(a, False)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)

def five():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)

def six():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)

def seven():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, False)

def eight():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)

def nine():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)

def zero():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, False)

try:
    while True:
        one()
        time.sleep(1)
        two()
        time.sleep(1)
        three()
        time.sleep(1)
        four()
        time.sleep(1)
        five()
        time.sleep(1)
        six()
        time.sleep(1)
        seven()
        time.sleep(1)
        eight()
        time.sleep(1)
        nine()
        time.sleep(1)
        zero()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

# 그냥 1357찍는거
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (21,20,16,26,19,12,13)
digits = (23,24,25,4)

for a in pin:
   GPIO.setup(a, GPIO.OUT)
   GPIO.output(a, 0)

for b in digits:
   GPIO.setup(b, GPIO.OUT)
   GPIO.output(b, 1)

list = {
   '0':(1,1,1,1,1,1,0,0), # 0
   '1':(0,1,1,0,0,0,0,0), # 1
   '2':(1,1,0,1,1,0,1,0), # 2
   '3':(1,1,1,1,0,0,1,0), # 3
   '4':(0,1,1,0,0,1,1,0), # 4
   '5':(1,0,1,1,0,1,1,0), # 5
   '6':(1,0,1,1,1,1,1,0), # 6
   '7':(1,1,1,0,0,1,0,0), # 7
   '8':(1,1,1,1,1,1,1,0), # 8
   '9':(1,1,1,1,0,1,1,0) # 9
   }

try:
   while True:

        for loop in range(0, 7):
            GPIO.output(pin[loop], list['1'][loop])

        GPIO.output(digits[0],0)
        time.sleep(0.5)
        GPIO.output(digits[0],1)
        

        for loop in range(0, 7):
            GPIO.output(pin[loop], list['3'][loop])

        GPIO.output(digits[1],0)
        time.sleep(0.5)
        GPIO.output(digits[1],1)
        

        for loop in range(0, 7):
            GPIO.output(pin[loop], list['5'][loop])

        GPIO.output(digits[2],0)
        time.sleep(0.5)
        GPIO.output(digits[2],1)
        

        for loop in range(0, 7):
            GPIO.output(pin[loop], list['7'][loop])

        GPIO.output(digits[3],0)
        time.sleep(0.5)
        GPIO.output(digits[3],1)

   
except KeyboardInterrupt:
   GPIO.cleanup()
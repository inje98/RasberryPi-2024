import RPi.GPIO as GPIO
import time

switch = 6
oldSw = 0
newSw = 0

com1 = 23
com2 = 24
com3 = 25

a = 21
b = 20
c = 16
d = 26
e = 19
f = 12
g = 13

index = 0

numAry = [[1,1,1,1,1,1,0], [0,1,1,0,0,0,0], [1,1,0,1,1,0,1], [1,1,1,1,0,0,1], [0,1,1,0,0,1,1], 
          [1,0,1,1,0,1,1], [1,0,1,1,1,1,1], [1,1,1,0,0,0,0], [1,1,1,1,1,1,1], [1,1,1,1,0,1,1]]

pinAry = [a, b, c, d, e, f, g]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(com1, GPIO.OUT)
GPIO.setup(com2, GPIO.OUT)
GPIO.setup(com3, GPIO.OUT)


for i in range(7):
    GPIO.output(pinAry)

# for i in pinAry:
#     GPIO.setup(i, GPIO.OUT)

# def display_number(number):
#     for i in range(7):
#         GPIO.output(pinAry[i], numAry[number][i])

# try:
#     while True:
#         newSw = GPIO.input(switch)
#         if newSw != oldSw:
#             oldSw = newSw

#             if newSw == 1:
#                 display_number(index)
#                 index += 1
#                 if index == 10:
#                     index = 0
#             time.sleep(0.2)
# except KeyboardInterrupt:
#     GPIO.cleanup()


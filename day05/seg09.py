import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = (21, 20, 16, 26, 19, 12, 13)
digits = (23, 24, 25, 4)

index1 = 0  
index2 = 0  
index3 = 0  
index4 = 0  

for a in pin:
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, 0)

for b in digits:
    GPIO.setup(b, GPIO.OUT)
    GPIO.output(b, 1)

list = {
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

def displayNum(index):
    for i in range(7):
        GPIO.output(pin[i], list[index][i])

try:
    while True:
        start_time = time.time()
        
        while time.time() - start_time < 1:
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

        index4 += 1
        if index4 == 10:
            index3 += 1
            index4 = 0
        if index3 == 10:
            index2 += 1
            index3 = 0
        if index2 == 10:
            index1 += 1
            index2 = 0
        if index1 == 10:
            index1 = 0
        
except KeyboardInterrupt:
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = (21, 20, 16, 26, 19, 12, 13)
digits = (23, 24, 25, 4)

trigPin = 18
echoPin = 17

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def measure():
    GPIO.output(trigPin, True)  
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    start = time.time()
    while GPIO.input(echoPin) == False:
        start = time.time()
    
    while GPIO.input(echoPin) == True:
        stop = time.time()
    
    elapsed = stop - start
    distance = (elapsed * 34300) / 2  
    return distance

def split_num(number):
    num = [int(i) for i in str(number).zfill(4)]
    return num

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
        distance = measure()
        #print("Distance: %.2f cm" %distance)
        print(int(distance))
        DistanceAry = split_num(int(distance))

        index1 = DistanceAry[0]
        index2 = DistanceAry[1]
        index3 = DistanceAry[2]
        index4 = DistanceAry[3]

        for _ in range(100):  
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

except KeyboardInterrupt:
    GPIO.cleanup()

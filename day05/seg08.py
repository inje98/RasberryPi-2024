# 1~9999 완성
import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (21,20,16,26,19,12,13)
digits = (23,24,25,4)

#switch
switch = 6
oldSw = 0
newSw = 0

index1 = 0 # 첫째자리
index2 = 0 # 둘째자리
index3 = 0 # 셋째자리
index4 = 0 # 넷째자리


GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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
   '9':(1,1,1,1,0,1,1,0)  # 9
   }

def displayNum(index):
    for i in range(7):
        GPIO.output(pin[i], list[index][i])

try:
   while True:
        newSw = GPIO.input(switch)
        

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
        
        if newSw != oldSw:
            oldSw = newSw

            if newSw == 1:
                print(str(index3)+str(index4))
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
                
            
            time.sleep(0.1)



                

except KeyboardInterrupt:
   GPIO.cleanup()
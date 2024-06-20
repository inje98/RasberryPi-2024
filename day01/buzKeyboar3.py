import RPi.GPIO as GPIO
import time

piezoPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)
Buzz.start(0) 

try:
    while True:
        getKey = int(input('Enter a number (1-8) to change frequency: '))
        
        if getKey == 1:
            Buzz.ChangeFrequency(130)
        elif getKey == 2:
            Buzz.ChangeFrequency(147)
        elif getKey == 3:
            Buzz.ChangeFrequency(165)
        elif getKey == 4:
            Buzz.ChangeFrequency(175)
        elif getKey == 5:
            Buzz.ChangeFrequency(196)
        elif getKey == 6:
            Buzz.ChangeFrequency(220)
        elif getKey == 7:
            Buzz.ChangeFrequency(247)
        elif getKey == 8:
            Buzz.ChangeFrequency(262)
        
        Buzz.ChangeDutyCycle(0.1) 
        time.sleep(0.1)  
        Buzz.ChangeDutyCycle(0) 
       # time.sleep(0.1) 

except KeyboardInterrupt:
    Buzz.stop()
    GPIO.cleanup()

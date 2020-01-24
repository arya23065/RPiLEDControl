import RPi.GPIO as GPIO
import time 

led1 = 16
led2 = 20
led3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)


while 1:
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led3, GPIO.LOW)
    
GPIO.cleanup()


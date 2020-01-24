//  the program will perform the periodic pattern of turning on one 
// LED for 1 sec, then turning it off and turning on the next LED for 
// 1 sec, and finally turning on the third LED for 1 sec, then repeating 
// from the top. 

import RPi.GPIO as GPIO
from time import sleep

# Pin Definitons:
led1 = 16 
led2 = 20
led3 = 21 

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(led1, GPIO.OUT) # LED pin set as output
GPIO.setup(led2, GPIO.OUT) # LED pin set as output
GPIO.setup(led3, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

try:
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
        else: # button is pressed:
            GPIO.cleanup()
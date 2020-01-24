import RPi.GPIO as GPIO
from time import sleep

# Pin Definitons:
led1 = 16 
led2 = 20
led3 = 21 
switch1 = 19
switch2 = 13

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(led1, GPIO.OUT) # LED pin set as output
GPIO.setup(led2, GPIO.OUT) # LED pin set as output
GPIO.setup(led3, GPIO.OUT) # LED pin set as output
GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

# Initial state for LEDs:
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)              


while True:

    if not(GPIO.input(switch1) or GPIO.input(switch2)):
        timecount = 0.0
        while timecount < 4:
            if (GPIO.input(switch1) or GPIO.input(switch2)) :
               break;
            if timecount < 2:
               GPIO.output(led1, 1)
               GPIO.output(led2, 1)
               GPIO.output(led3, 1)
            else :
               GPIO.output(led1, 0)
               GPIO.output(led2, 0)
               GPIO.output(led3, 0)
            sleep(0.2)
            timecount += 0.2
    elif (GPIO.input(switch1) and GPIO.input(switch2)):
        GPIO.output(led1, 0)
        GPIO.output(led2, 0)
        GPIO.output(led3, 0)
        sleep(0.2)
    else:
        timecount = 0.0
        while timecount < 3.0 :
            if GPIO.input(switch1) == GPIO.input(switch2) :
                    break;
            if timecount < 1.0 :
                        GPIO.output(led3, 0)
                        GPIO.output(led1, 1)
            elif timecount < 2.0 :
                        GPIO.output(led1, 0)
                        GPIO.output(led2, 1)
            else :
                        GPIO.output(led2, 0)
                        GPIO.output(led3, 1)
            timecount += 0.2
            sleep(0.2)
           
               
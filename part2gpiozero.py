

from gpiozero import LED, Button
from time import sleep
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)

switch1 = Button(19)
switch2 = Button(13)

while True:
    if switch1.is_pressed and switch2.is_pressed:
        timecount = 0.0
        while timecount < 4.0:
            if not(switch1.is_pressed and switch2.is_pressed):
                break;
            if (timecount < 2.0):
                led1.on()
                led2.on()
                led3.on()
            else:
                led1.off()
                led2.off()
                led3.off()  
            sleep(0.2)   
            timecount += 0.2
    elif not(switch1.is_pressed or switch2.is_pressed):
        led1.off()
        led2.off()
        led3.off()
        sleep(0.2)
    else:
        timecount = 0.0
        while timecount < 3.0:
            if switch1.is_pressed == switch2.is_pressed :
                break;
            if timecount < 1.0 :
               led3.off()
               led1.on()
            elif timecount < 2.0 :
               led1.off()
               led2.on()
            else :
               led2.off()
               led3.on()
            timecount += 0.2
            sleep(0.2)
           

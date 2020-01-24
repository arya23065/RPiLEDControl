//  the program will perform the periodic pattern of turning on one 
// LED for 1 sec, then turning it off and turning on the next LED for 
// 1 sec, and finally turning on the third LED for 1 sec, then repeating 
// from the top. 

from gpiozero import LED
from time import sleep

led1 = LED(16)
led2 = LED(20)
led3 = LED(21)

while True:
    led3.off()
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    led3.on()
    sleep(1)
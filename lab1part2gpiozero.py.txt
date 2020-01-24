//Modify your Python3 program to add the on/off functionality by reading from the switches.
// The program should check the switches every 200 milliseconds and react as follows:
// - If both switches are off, the program turns all LEDs off.
// - If both switches are on, the program turns all LEDs on for 2 sec and turns them all off for 2 sec.
// - If one switch is on and the other off, the program will perform the periodic pattern of turning
// on one LED for 1 sec, then turning it off and turning on the next led for 1 sec, and finally turning
// on the third LED for 1 sec.

from gpiozero import LED, Button
from time import sleep
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)

switch1 = Button(19)
switch2 = Button(13)

while True:
    if switch1.is_pressed and switch2.is_pressed:
	float timecount = 0.0
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
	float timecount = 0.0
	while timecount < 3.0
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
           

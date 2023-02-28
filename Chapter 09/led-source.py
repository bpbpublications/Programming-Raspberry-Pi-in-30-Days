#import libraries
from gpiozero import Button, LED
from signal import pause

#Define LED and button
led = LED(27)
button = Button(17)

# Feed the values of the button into the LED
led.source = Button

#Run the code indefinitely
pause()
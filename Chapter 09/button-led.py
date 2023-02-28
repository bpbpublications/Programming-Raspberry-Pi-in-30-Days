#import libraries
from gpiozero import LED, Button
from signal import pause

#Define the LED and button
led = LED(17)
button = Button(27)

#Turn the LED on when the button is pressed
button.when_pressed = led.on()
button.when_pressed = led.off()

# Run the code indefinitely
pause()
#import libraries
from gpiozero import PWMLED
from signal import pause

# Define the LED
led = PWMLED(17)

# Use pulse to change the brightness of the LED
led.pulse()

#Keep the script alive
pause()
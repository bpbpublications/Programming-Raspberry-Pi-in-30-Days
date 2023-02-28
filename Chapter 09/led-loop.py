#import libraries
from gpiozero import LED
from signal import pause

# Define the LED
led = LED(17)

# Blink the LED using blink indefinitely
led.blink()

#Keep the script running
pause()
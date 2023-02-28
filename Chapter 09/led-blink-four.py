#import libraries
from gpiozero import LED
from signal import pause

# Define the LED

led = LED(17)

# Use blink to blink the LED four times
led.blink(n=4)

# Keep the script alive with this
pause()

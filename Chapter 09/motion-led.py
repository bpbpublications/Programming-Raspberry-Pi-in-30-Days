#import libraries
from gpiozero import MotionSensor, LED
from signal import pause

#Define the sensor and LED
pir = MotionSensor(17)
led = LED(27)

#Turn LED on or off based on motion
pir.when_motion = led.on
pir.when_no_motion = led.off

#Code should run indefinitely
pause()
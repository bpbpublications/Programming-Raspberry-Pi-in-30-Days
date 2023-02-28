#import libraries
from gpiozero import MotionSensor, Robot
from signal import pause

#Define the sensor and LED
pir = MotionSensor(22)
robot = Robot(left=(13, 21), right=(17, 27))

#Move robot based on motion
pir.when_motion = robot.forward
pir.when_no_motion = robot.stop

#Code should run indefinitely
pause()
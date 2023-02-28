#import libraries
from gpiozero import MotionSensor

#Define the sensor
pir = MotionSensor(17)

#Wait for motion
pir.wait_for_motion()
print("Motion Detected")
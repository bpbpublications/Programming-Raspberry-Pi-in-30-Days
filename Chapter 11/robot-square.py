# Import libraries
from gpiozero import Robot
from time import sleep

#Define the robot
robot = Robot(left=(13, 21), right=(17, 27))

#Move the robot in a square
for i in range(1, 5):
    robot.forward()
    sleep(2)
    robot.left()
    sleep(0.5)
 
    
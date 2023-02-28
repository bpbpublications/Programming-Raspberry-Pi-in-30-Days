# Import libraries
from gpiozero import Robot
from time import sleep

#Define the robot
robot = Robot(left=(13, 21), right=(17, 27))

#Move the robot forward and backward
robot.forward()
sleep(1)
robot.backward()
sleep(1)
robot.left()
sleep(1)
robot.right()
sleep(1)
robot.stop()
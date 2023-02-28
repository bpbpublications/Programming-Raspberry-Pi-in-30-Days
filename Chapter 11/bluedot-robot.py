# Import Libraries
from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

# Define our dot and robot
bd = BlueDot()
robot = Robot(left=(13, 21), right=(17, 27))

# Define our positions
def move(pos):
    if pos.top:
        robot.forward()
    elif pos.bottom:
        robot.backward()
    elif pos.left:
        robot.left()
    elif pos.right:
        robot.right()

# Define our stop function
def stop():
    robot.stop()

#Define our parameters
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

#Keep the code running
pause()
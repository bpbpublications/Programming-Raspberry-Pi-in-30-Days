#Import our libraries
from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

# Define our bluedot and robot
bd = BlueDot()
robot = Robot(left=(13, 21), right=(17, 27))

# Here we define the movement based on distance from the direction
def move(pos):
    if pos.top:
        robot.forward(pos.distance)
    elif pos.bottom:
        robot.backward(pos.distance)
    elif pos.left:
        robot.left(pos.distance)
    elif pos.right:
        robot.right(pos.distance)

# Here we stop the robot
def stop():
    robot.stop()

# We define our parameters
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

# We keep the app running 
pause()

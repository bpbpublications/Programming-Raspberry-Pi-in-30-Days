#import libraries
import curses
from gpiozero import Robot
from picamera import PiCamera
from datetime import datetime

#define the camera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25
moment = datetime.now()

#Define the Robot
robot = robot(left=(13, 21), right=(17, 27))

#Define the actions
actions = {
    curses.KEY_UP:    robot.forward(),
    curses.KEY_DOWN:  robot.backward(),
    curses.KEY_LEFT:  robot.left(),
    curses.KEY_RIGHT: robot.right(),
}
#Define our record and stop record buttons
def record():
    camera.start_recording('/home/pi/Videos/video_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    camera.stop_recording()

#Define the function here
def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY IS PRESSED
            # Adds a three second delay between presses
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            # This indicates when the next key is pressed
            while next_key == key:
                next_key = window.getch()
            # KEY IS RELEASED
            robot.stop()
        if key == ord('q'):
            break # quit the loop gracefully
        if key == ord('r'):
            record() # Enable the camera
        if key == ord('s'):
            stop_record() # Stop recording
# This runs the function and wraps it with curses
curses.wrapper(main)
camera.stop_recording()
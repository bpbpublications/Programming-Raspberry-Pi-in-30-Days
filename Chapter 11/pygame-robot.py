# Import the libraries
import pygame
from gpiozero import Robot
from picamera import PiCamera
from datetime import datetime

#define the camera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 25
moment = datetime.now()

#define robot
robot = Robot(left=(13, 21), right=(17, 27))

#We must open a Pygame window to allow it to detect user events
screen = pygame.display.set_mode([240, 160])

#Define our record and stop record buttons
def record():
    camera.start_recording('/home/pi/Videos/video_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    camera.stop_recording()

# Here we open the window and then press keys to control the directions of the robot
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				robot.right()
			if event.key == pygame.K_LEFT:
				robot.left()
			if event.key == pygame.K_UP:
				robot.forward()
			if event.key == pygame.K_DOWN:
				robot.backward()
			if event.key == pygame.K_q:
				pygame.quit()
                        if event.key == pygame.K_r:
                                record()
                        if event.key == pygame.K_s:
                                stop_record()
		elif event.type == pygame.KEYUP:
			robot.stop()


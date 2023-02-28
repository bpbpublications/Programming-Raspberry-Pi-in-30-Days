#import libraries
from gpiozero import Button
from picamera import PiCamera

#define button
button = Button(17)

#Define the camera and resolution
camera = PiCamera()
camera.resolution = (1280, 720)

#Start with the frame equal to one
#We loop through the images created and iterate by one
while True:
    button.wait_for_press()
    camera.capture("/home/pi/Pictures/frame%03d.jpg" % frame)
    frame += 1
#Import libraries
from gpiozero import AngularServo
from time import sleep

#Define the angular servo
angular_servo = AngularServo(17, min_angle=-90, max_angle=90)

#Move the servo based on the angles
while True:
    angular_servo.angle = -90
    sleep(1)
    angular_servo.angle = -45
    sleep(1)
    angular_servo.angle = 0
    sleep(1)
    angular_servo.angle = 45
    sleep(1)
    angular_servo.angle = 90
    sleep(1)
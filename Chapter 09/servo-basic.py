#import libraries
from gpiozero import Servo
from time import sleep

#Define the servo
servo = Servo(17)

#Change among its min, mid and max positions
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
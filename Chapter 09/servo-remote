#import libraries
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from time import sleep

#Define our factory
factory = PiGPIOFactory(host='192.168.0.12')

#Define the servo
servo = Servo(17, pin_factory=factory)

#Change among its min, mid and max positions
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
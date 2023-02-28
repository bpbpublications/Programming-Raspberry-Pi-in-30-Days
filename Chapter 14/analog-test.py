from machine import ADC
from utime import sleep

pot = ADC(26)

while True:
    print(pot.read_u16())
    sleep(2)

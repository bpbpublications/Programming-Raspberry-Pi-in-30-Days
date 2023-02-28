#import libraries
from gpiozero import Button

#define the button
button = Button(17)

#Print a statement when the button is pressed
button.wait_for_press()
print("Button pressed")
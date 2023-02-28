#import libraries
from guizero import App, PushButton, Text
from gpiozero import LEDBoard

#Define the leds
traffic_lights = LEDBoard(17, 27, 22)

#Define the functions for each button
def stoplight():
    traffic_lights.value = (1, 0, 0)

def slowlight():
    traffic_lights.value = (0, 1, 0)

def golight():
    traffic_lights.value = (0, 0, 1)
    

#Define the app
app = App(title="Traffic Lights")
app.bg = "aqua"

#Create the title
traffic = Text(app, text="Traffic Light Control")
traffic.text_size = 20

#Create the buttons
stop = PushButton(app, text="STOP", command=stoplight)
stop.bg = "red"
stop.text_size = 20
slow = PushButton(app, text="SLOW", command=slowlight)
slow.bg = "yellow"
slow.text_size = 20
go = PushButton(app, text="GO", command=golight)
go.bg = "green"
go.text_size = 20

#display the app
app.display()
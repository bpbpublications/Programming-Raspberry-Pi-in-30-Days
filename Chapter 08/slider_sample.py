#Import the App and Text Widget from Guizero
from guizero import App, Text, Slider

#Define a function to change the text value
def change_size(slider_value):
    message.text_size = slider_value
    
# Define the app with the title hello world
app = App(title="Hello World")
# Add color to our app
app.bg = "#41f1e6"
# Add a message to the app
message =Text(app, text="Move the Slider Using the Mouse")
# Add a slider to the app
slider_sample = Slider(app, start=20, end=40, command=change_size)
# Add color to our slider
slider_sample.bg = "#f141e1"
# Display the app
app.display()
#Import the App, Text, PushButton, Slider and Window Widget from Guizero
from guizero import App, Text, PushButton, Window, Slider

# Add this function to our button
def press_button():
    print("Button clicked")

def release_button():
    print("Button released")

def change_size(slider_value):
    message.text_size = slider_value

# Define the app with the title Button Press
app = App(title="Button Press")
# Add background color to the app
app.bg = "#41f18e"
# add a window for the slider and color
slider_window = Window(app, "Slider Window")
slider_window.bg ="aqua"
# Add a message to the app
message =Text(app, text="Press the Button")
# Change the text size to the app
message.text_size = 25
# Add the push button
button = PushButton(app, text="Press")
# Add background color to button
button.bg = "#e6f141"
# Change button text size
button.text_size = 20
# add a command for when the button is pressed
button.when_left_button_pressed = press_button
# add a command for when the button is released
button.when_left_button_released = release_button

# Add a message to the app
message =Text(slider_window, text="Move the Slider Using the Mouse")
# Add a slider to the app
slider_sample = Slider(slider_window, start=20, end=40, command=change_size)
# Add color to our slider
slider_sample.bg = "#f141e1"
# Display the app
app.display()
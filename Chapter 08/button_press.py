#Import the App, Text and PushButton Widget from Guizero
from guizero import App, Text, PushButton

# Add this function to our button and slider
def press_button():
    print("Button clicked")

def release_button():
    print("Button released")

# Define the app with the title Button Press
app = App(title="Button Press")
# Add background color to the app
app.bg = "#41f18e"
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
# Display the app
app.display()
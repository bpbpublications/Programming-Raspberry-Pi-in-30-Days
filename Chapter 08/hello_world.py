#Import the App and Text Widget from Guizero
from guizero import App, Text

# Define the app with the title hello world
app = App(title="Hello World")
# Add background color to decorate the app
app.bg = "aqua"
# Add a message to the app
message =Text(app, text="Welcome to my first app")
# Change the text size of the message to 20
message.text_size = 20

# Display the app
app.display()
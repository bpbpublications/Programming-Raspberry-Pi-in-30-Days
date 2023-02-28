#import widgets
from guizero import App, Drawing, Slider, Combo, Box, Text

# Add this function so that when the mouse is pressed it will start drawing
# This updates our shpaes
def start(event):
    painting.last_event = event 
    painting.first_event = event
    painting.last_shape = None

#define draw function for our drawing widget
# Here an event is created using the x and y positions
# The event here is a mouse action
# This is updated to ensure the last event is updated to event
# This is updated to allow the line to have different widths and colors
def draw(event):
    # If the shape is a line it will draw a line
    if shapes.value == "line":
        painting.line(
        painting.last_event.x - 1, painting.last_event.y - 1,
        event.x + 1, event.y + 1,
        color=color.value, width = width.value)
    # If it is a rectangle it will draw and delete until the mouse is released
    if shapes.value == "rectangle":
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        rectangle = painting.rectangle(painting.first_event.x, painting.first_event.y, event.x, event.y, color=color.value)
        painting.last_shape = rectangle 
    painting.last_event = event


#Define the app and background
app = App("Paint Program")
app.bg = "white"

# Add a box for our widgets
menu = Box(app, align="top", width="fill", border=True)

# Add text for our color widget
Text(menu, text="Color", align="left")
# Define the drop down menu for color
color = Combo(menu, options=["red", "orange", "yellow", "green", "blue", "purple"], align="left")

# Add text for our slider
Text(menu, text="Width", align="left")
# Define our slider for the width
width = Slider(menu, start=1, end=10, align="left")

# Add text for our shapes combo
Text(menu, text="Shapes", align="left")
# Define another combo for our shapes
shapes = Combo(menu, options=["line", "rectangle"], align="left")
# Define the drawing
painting = Drawing(app, width="fill", height="fill")

# Connect the function to the drawing widget
painting.when_mouse_dragged = draw

# Add this to ensure that the drawing widget updates when it is clicked
painting.when_left_button_pressed = start

# Display the app
app.display()
#import libraries
from guizero import App, PushButton, Drawing, TextBox, Combo, Slider
from picamera import PiCamera

#Define the camera with a smaller resolution
camera = PiCamera(resolution="400x400")

#Define our function for the camera
def capture_image():
    camera.capture("image.jpg")
    viewer.image("image.jpg")
    viewer.text(20, 20, top_text.value, color=color.value, size=font.value)
    viewer.text(20, 320, bottom_text.value, color=color.value, size=font.value)

#Define our app
app = App(title="Meme Generator")
app.bg = "white"

#Define our Push Button, textbox and Picture widgets
picture = Pushbutton(app, text="Take Picture", command=capture_image)
picture.text_size = 20
picture.bg = "yellow"
top_text = TextBox(app, text="top text")
top_text.text_size = 15
bottom_text = TextBox(app, text="bottom text")
bottom_text.text_size = 15
color = Combo(app, options=["red", "black", "aqua", "green", "yellow", "pink"]
color.text_size = 15
font = Slider(app, start=20, end=50)
font.text_size = 15
font.bg = "aqua"
viewer = Drawing(app, width="fill", height="fill")

#display app
app.display()
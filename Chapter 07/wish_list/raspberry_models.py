import sqlite3

models = [
    "Model B",
    "Model B+",
    "Model A",
    "Model A+",
    "Pi 3 Model A+",
    "Pi 2",
    "Pi Zero",
    "Pi Zero W",
    "Pi Zero W 2",
    "Pi 3",
    "Pi 3 Model B+",
    "Pi 4",
    "Pi 400",
    "Pico"
]

# This sorts the Pi Models
models = sorted(models)

# Connect to a database
connection = sqlite3.connect("raspberrypi.db")

# Create a cursor to execute commands
cur = connection.cursor()

# Create the table here
cur.execute("CREATE TABLE models (name TEXT)")
# Loop through the models table to add new entries
for i in range(len(models)):
    cur.execute("INSERT INTO models (name) values (?)", [models[i]])
    print("Added", models[i])

connection.commit()
connection.close()
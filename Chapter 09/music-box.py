#import libraries
import pygame
from gpiozero import Button, LEDBoard

#initialize pygame
pygame.init()

#setup the instruments
drum = pygame.mixer.Sound("/home/pi/Documents/music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/Documents/music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/Documents/music-box/samples/drum_snare_hard.wav")
cowbell = pygame.mixer.Sound("/home/pi/Documents/music-box/samples/drum_cowbell.wav")

#Define the LEDs
music_leds = LEDBoard(12, 16, 20, 21)

#Define the buttons for the sounds
button_drum = Button(4)
button_cymbal = Button(17)
button_snare = Button(27)
button_snare = Button(22)

# Define the functions for each button
def drum_play():
    music_leds.value = (1, 0, 0, 0)
    drum.play()

def cymbal_play():
    music_leds.value = (0, 1, 0, 0)
    cymbal.play()

def snare_play():
    music_leds.value = (0, 0, 1, 0)
    snare.play()

def cowbell_play():
    music_leds.value = (0, 0, 0, 1)
    cowbell.play()

#Connect the functions to the buttons
button_drum.when_pressed = drum_play
button_drum.when_released = music_leds.off()
button_cymbal.when_pressed = cymbal_play
button_cymbal.when_released = music_leds.off()
button_snare.when_pressed = snare_play
button_snare.when_released = music_leds.off()
button_cowbell.when_pressed = cowbell_play
button_cowbell.when_released = music_leds.off()
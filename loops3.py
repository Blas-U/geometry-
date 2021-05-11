#make lights 5 through 10 blue
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (0,20,2):
    pixels[i] = (0, 0, 255)

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (0,20):
    pixels[i] = (0, 0, 0)

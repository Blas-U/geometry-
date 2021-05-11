#backwards lights light up .25 seconds between each lighing up
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i range (20,0):
    pixels[i] = (255, 69, 0)
    time.sleep (.25)

for x in range (1):
    pixels[x] = (255, 69, 0)
    time.sleep (.25)

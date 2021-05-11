#lights1.py
#Light the 4th light

	import board
	import neopixel

	pixels = neopixel.NeoPixel(board.D18, 20)

	pixels[4] = (10,0,0)

#lights2.py
#2nd Light green

	import board
	import neopixel

	pixels = neopixel.NeoPixel(board.D18, 20)

	pixels[1] = (34,139,34)

#lights3.py
#4th light yellow
	import board
	import neopixel

	pixels = neopixel.NeoPixel(board.D18, 20)

	pixels[3] = (255,255,0)

#lights4.py
#Light up the first 5 lights

	import board
	import neopixel

	pixels = neopixel.NeoPixel(board.D18, 20)

	for i in range(5):
        	pixels[i] = (10,0,0)

#lights5.py
#Light up the first 16 lights

	import board
	import neopixel

	pixels = neopixel.NeoPixel(board.D18, 20)

	for i in range(15):
        	pixels[i] = (10,0,0)

#lights6.py
#first 5 red rest blue

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

For i in range (4):
	Pixels[i] = (255,0,0)

For i in range (5, 20):
	Pixels[i] = (0,0,10)

#lights7.py
#all lights up one at a time with .25 seconds between

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range(0):
	pixels[i] = (255,69,0)
	time.sleep(.1)

for x in range (20):
	pixels[x] = (69,69,69)
	time.sleep(.25)

#lights8.py
#over 2.5 march across the strip

for i in range(0,20)
	pixels[i] = (0,0,0)

for x in range(0,20)
	pixels[x] = (255,255,255)
	time.sleep(2.5)

for y in range(0,20):
	pixels[y] = (0,0,0)
	time.sleep(2.7)

#loops1.py
#make last 5 lights red

for i in range(14,20):
	pixels[i] = (255,0,0)

loops2.py
light 5 through 10 blue

for i in range(4,9):
	

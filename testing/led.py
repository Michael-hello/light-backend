#import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
#print "LED on"
#GPIO.output(18,GPIO.HIGH)
#time.sleep(1)
#print "LED off"
#GPIO.output(18,GPIO.LOW)

import board
import neopixel
#pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
pixels = neopixel.NeoPixel(board.D18, 30)
pixels.fill((0, 255, 0))
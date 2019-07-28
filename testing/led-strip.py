import board
import digitalio
import busio
import neopixel
import time

print("Hello blinka!")

 
# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")
 
# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")
 
# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")
 
print("done!")

brightness = 0

pixels = neopixel.NeoPixel(board.D18, 60, brightness=brightness)
pixels.fill((255, 255, 255))

time.sleep(1)
#pixels.fill((0, 255 , 0))
brightness = 0.1
pixels.show()



#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
from Adafruit_I2C import Adafruit_I2C

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
i2CBus = Adafruit_I2C.getPiI2CBusNumber()

# if using this example with a BeagleBone, uncomment the line below and specify
# which I2C Bus the backpack is connected on. If connected to I2C1 (Header P9, 
# pin 17 & 18) specify 1, if connected to I2C2 (Header P9, pin 19 & 20) specify 3.
# WARNING: if using with a BeagleBone use a logic-level convertor such as this one
# https://www.adafruit.com/products/757
# i2CBus = 1 | 3

grid = EightByEight(address=0x70, bus=i2CBus)

print "Press CTRL+Z to exit"

# Continually update the 8x8 display one pixel at a time
while(True):
  for x in range(0, 8):
    for y in range(0, 8):
      grid.setPixel(x, y)
      time.sleep(0.05)
  time.sleep(0.5)
  grid.clear()
  time.sleep(0.5)

#!/usr/bin/python

import time
import datetime
from Adafruit_7Segment import SevenSegment
from Adafruit_I2C import Adafruit_I2C

# ===========================================================================
# Clock Example
# ===========================================================================
i2CBus = Adafruit_I2C.getPiI2CBusNumber()

# if using this example with a BeagleBone, uncomment the line below and specify
# which I2C Bus the backpack is connected on. If connected to I2C1 (Header P9, 
# pin 17 & 18) specify 1, if connected to I2C2 (Header P9, pin 19 & 20) specify 3.
# WARNING: if using with a BeagleBone use a logic-level convertor such as this one
# https://www.adafruit.com/products/757
i2CBus = 3

segment = SevenSegment(address=0x70, bus=i2CBus)

print "Press CTRL+Z to exit"

# Continually update the time on a 4 char, 7-segment display
while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  # Set hours
  segment.writeDigit(0, int(hour / 10))     # Tens
  segment.writeDigit(1, hour % 10)          # Ones
  # Set minutes
  segment.writeDigit(3, int(minute / 10))   # Tens
  segment.writeDigit(4, minute % 10)        # Ones
  # Toggle color
  segment.setColon(second % 2)              # Toggle colon at 1Hz
  # Wait one second
  time.sleep(1)

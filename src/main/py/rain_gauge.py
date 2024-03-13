from gpiozero import Button
from time import sleep
import math

# This is a program to read inputs from the rain gauge sensor, bought from the 
# RaspberryPi documentation to build a weather station.
# The main functionality of this sensor is to send an interrupt each time the
# tank fills up.
# The tank is about 0.2794 mm, so the main goal of this program is to check
# each CHECK_TIME seconds the input to see if the tank was filled and emptied 
# in that time step.

# Global variables
rain_sensor = Button(6) # We use BCM 6 GPIO which has phisical address 31
count = 0 # global counter of the tanks fills

# Macros
BUCKET_SIZE = 0.2794 # mm
CHECK_TIME = 5 # sec


def bucket_tipped():
    global count
    count += 1

def bucket_reset():
    global count
    count = 0


# This fuction return the mm observed in the CHECK_TIME time step 
def read_bucket_fills():
    return count * BUCKET_SIZE


rain_sensor.when_pressed = bucket_tipped
#rain_sensor.when_released = bucket_reset


while True:
    count = 0
    sleep(CHECK_TIME)
    print(str(read_bucket_fills()))



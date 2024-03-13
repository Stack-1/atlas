import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL,board.SDA)

ads = ADS.ADS1015(i2c)
chan_1 = AnalogIn(ads,ADS.P0)

count=0
values=[]

while True:
    wind = round(chan_1.voltage,1)
    if not wind in values:
        values.append(wind)
        count+=1
        print(count)

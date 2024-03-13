import bme280
import smbus
from time import sleep

port = 1
address = 0x76
bus = smbus.SMBus(port)
sleep(1)

bme280.load_calibration_params(bus,address)

# while True:
bme280_data=bme280.sample(bus,address)
humidity = bme280_data.humidity
temperature = bme280_data.temperature
preassure = bme280_data.pressure
print("Temperature is: " + str(temperature) + " °C\nHumidity is: \t" + str(humidity) + " %\nPreassure is: \t" + str(preassure) + " mBar")
	# sleep(1)

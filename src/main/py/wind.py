from gpiozero import Button
from signal import pause


GPIO_WIND_SENSOR = 5

wind_speed_sensor = Button(GPIO_WIND_SENSOR)
wind_count = 0

def spin():
	global wind_count
	wind_count = wind_count + 1
	print("spin " + str(wind_count))

wind_speed_sensor.when_pressed = spin

pause()

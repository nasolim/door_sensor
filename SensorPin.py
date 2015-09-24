import time
import RPi.GPIO as io
import SensorClient as sensor

io.setmode(io.BCM)
pin=18

io.setup(18,io.IN,pull_up_down=io.PUD_DOWN)

while True:
	io.wait_for_edge(pin,io.RISING)
	sensor.Main('War_Room:1')
	
	io.wait_for_edge(pin,io.FALLING)
	sensor.Main('War_Room:0')
	
io.cleanup()
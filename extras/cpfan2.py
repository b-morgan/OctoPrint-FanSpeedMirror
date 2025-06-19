#!/home/pi/env/bin/python3
import datetime
import time
import board
import sys
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
# get the speed from 0 (off) to 255 (max speed)
if len(sys.argv) >= 2:
	s = int(float(sys.argv[1])+0.5)
else:
	s = 0
# fans won't run at really low speeds so don't try
if s < 32:
	kit.motor3.throttle = 0
	kit.motor4.throttle = 0
else:
# make sure speed is in range
	s = min(s,255)
	if s < 80:
# for low speeds, goose the fan to get it started
		kit.motor3.throttle = 0.75
		kit.motor4.throttle = 0.75
		time.sleep(0.05)
# set the fan speed
	t = float(s)/255.0
# do both fans
	kit.motor3.throttle = t
	kit.motor4.throttle = t

now = datetime.datetime.now()
o = open("/home/pi/cpfan2.log", "a")
o.write(now.strftime("%Y-%m-%d %H:%M:%S") + " set speed to " + str(s) + "\n")
if sys.prefix != sys.base_prefix:
    o.write("Currently running in a virtual environment.\n")
    o.write(f"Virtual environment path: {sys.prefix}\n")
else:
    o.write("Not running in a virtual environment.\n")
o.close()

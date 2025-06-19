#!/home/pi/env/bin/python3
import datetime
import sys
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
# turn the fans off
kit.motor3.throttle = 0
kit.motor4.throttle = 0

now = datetime.datetime.now()
o = open("/home/pi/cpfan2.log", "a")
o.write(now.strftime("%Y-%m-%d %H:%M:%S") + " set speed to Off\n")
if sys.prefix != sys.base_prefix:
    o.write("Currently running in a virtual environment.\n")
    o.write(f"Virtual environment path: {sys.prefix}\n")
else:
    o.write("Not running in a virtual environment.\n")
o.close()

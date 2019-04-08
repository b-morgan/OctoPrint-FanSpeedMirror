#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import sys

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
# get the speed from 0 (off) to 255 (max speed)
s = int(float(sys.argv[1])+0.5)
# do both fans
for f in [3,4]:
    myMotor = mh.getMotor(f)
# fan won't run at really low speeds so don't try
    if s < 32:
        myMotor.run(Adafruit_MotorHAT.RELEASE)
    else:
# make sure speed is in range
        s = min(s,255)
        myMotor.run(Adafruit_MotorHAT.FORWARD)
        if s < 80:
# for low speeds, goose the fan to get it started
            myMotor.setSpeed(192)
            time.sleep(0.05)
# set the fan speed
        myMotor.setSpeed(s)

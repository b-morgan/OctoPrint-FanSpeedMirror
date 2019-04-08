#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# disable motor(s)
myMotor = mh.getMotor(3)
myMotor.run(Adafruit_MotorHAT.RELEASE)
myMotor = mh.getMotor(4)
myMotor.run(Adafruit_MotorHAT.RELEASE)

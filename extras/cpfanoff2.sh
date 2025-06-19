#!/bin/bash
echo $1 $2 $3 >>/home/pi/fan.txt
/home/pi/env/bin/python3 /home/pi/cpfanoff2.py $1 >>/home/pi/cpfan2.txt
exit $?

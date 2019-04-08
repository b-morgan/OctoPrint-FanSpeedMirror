#!/bin/bash
echo $1 $2 $3 >>/home/pi/fan.txt
python /home/pi/fan.py $1
exit $?
 

#!/bin/bash
echo "Off" $1 $2 $3 >>/home/pi/fan.txt
python /home/pi/fanoff.py $1
exit $?
 

#!/bin/bash
echo "Off" $1 $2 $3 >>/home/pi/fan.txt
python /home/pi/fanoff2.py $1
exit $?
 

#!/bin/bash
echo $1 $2 $3 >>/home/pi/fan.txt
python /home/pi/fan2.py $1
exit $?
 

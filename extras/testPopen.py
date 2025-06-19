#!/usr/bin/python3
import datetime
import time
import sys
import subprocess

# get the command to execute and the speed from 0 (off) to 255 (max speed)
if len(sys.argv) >= 3:
	cmd_line = sys.argv[1]
	s = int(float(sys.argv[2])+0.5)
else:
	print("Need some data to get going")
	exit()

s = min(s,255)
t = float(s)/255.0
print("Executing (" + cmd_line + ")")
try:
	p = subprocess.Popen([cmd_line, str(s)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	o = p.communicate()[0]
	r = p.returncode
#	print("Command %s returned: %s, o=%s" % (cmd_line, r, o))
	if r != 0:
		print("Error executing command %s: r=%s", o=%s % (cmd_line, r, o))
except OSError as e:
	print("Exception executing command %s: %s" % (cmd_line, e))

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S") + " set speed to " + str(s))

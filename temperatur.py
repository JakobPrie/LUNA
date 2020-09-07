import subprocess
from time import sleep

while True:
	temp = subprocess.call(["vcgencmd", "measure_temp"])
	#print(temp)
	sleep(3600)

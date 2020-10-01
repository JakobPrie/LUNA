import datetime
import subprocess


INTERVALL = 600

def run(luna, profile):
	lauter = "amixer scontrols 100%"
	leise = "amixer scontrols 40%"
	
	next_change = luna.module_storage["next_change"]
	
	stunde = datetime.datetime.now().hour
	
	if stunde >= 6 and stunde <= 22 and next_change == "higher":
		print('--> Lautstärke wird erhöht!')
		subprocess.Popen(lauter.split(' '))
		luna.module_storage["next_change"] = "lower"
	
	elif stunde >= 22 and next_change == "lower":
		print('--> Lautstärke wird verniedrigt!')
		subprocess.Popen(leiser.split(' '))
		luna.module_storage["next_change"] = "higher"

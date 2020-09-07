import subprocess
from time import sleep

PRIORITY = 9

def isValid(text):
	text = text.lower()
	if 'wie' in text and 'du' in text and ('warm' in text or 'heiß' in text):
		return True
	elif 'welche' in text and 'temperatur' in text and 'du' in text:
		return True 

def handle(text, luna, profile):
	temp = subprocess.call(["vcgencmd", "measure_temp"])
	print(temp)
	luna.say('Die CPU ist derzeit ' + temp + ' Grad Celsius warm.')

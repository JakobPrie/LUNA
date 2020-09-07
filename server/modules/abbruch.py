PRIORITY = 9
SECURE = True

def isValid (text):
	text = text.lower()
	if 'abbruch' in text:
		return True
	elif 'abbrechen' in text:
		return True
	
def handle (text, luna, profile):
	print('Befehl abgebrochen')
	#luna.say('Befehl abgebrochen')

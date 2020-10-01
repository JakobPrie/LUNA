

def isValid(text):
	if 'stopp' in text:
		return True
	elif 'ich' in text and 'bin' in text and 'wach' in text:
		return True
	else:
		return False
	
def handle(text, luna, profile):
	luna.Audio_Output.stop_playback

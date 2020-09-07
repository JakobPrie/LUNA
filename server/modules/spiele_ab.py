import wave


def isValid(text):
	text = text.lower()
	if 'server' in text and 'ab' in text:
		return True
	
def handle(text, luna, profile):
	audio = wave.open('/home/pi/Desktop/LUNA/Schlafzimmer/modules/resources/tagesschau_100sec.wav', 'rb')
	luna.play(audio)

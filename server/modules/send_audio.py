import wave

def isValid(text):
	text = text.lower()
	if 'spiele' in text and 'ab' in text:
		return True
		
def handle(text, luna, profile):
	text = text.lower()
	print("Play-Audio")
	audio = wav = wave.open("/home/pi/Desktop/LUNA/Schlafzimmer/temp16.wav", 'rb')
	print("luna.play(audio) aufgerufen...")
	luna.play(audio=audio, user=luna.user)
	

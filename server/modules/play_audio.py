
def isValid(text):
	text = text.lower()
	if 'spiel' in text and 'ab' in text:
		return True
	
def handle(text, luna, profile):
	luna.play(path="/home/pi/Desktop/LUNA/server/modules/resources/aufstehen.wav", room='Schlafzimmer')
	print("Modul abgeschlossen...")

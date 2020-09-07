SECURE = False

def isValid(text):
	if 'hotworddetection' in text:
		return True
	
def handle(text, luna, profile):
	room = luna.analyze["room"]
	if room is None:
		room = luna.room_name
			
	if 'start' in text: 
		luna.start_module(name='start_hotword_detection', room=room, text=text)
	elif 'stopp' in text:
		luna.start_module(name='stopp_hotword_detection', room=room, text=text)

SECURE = False

def isValid(text):
	if 'hotworddetection' in text:
		return True
	
def handle(text, luna, profile):
	room = luna.analyze["room"]
	if room is None:
		room = luna.room_name
			
	if 'start' in text: 
		luna.change_hotworddetection(room=room, changing_to='on')
		luna.say("Die Hotworddetection wurde eingeschaltet, ab jetzt höre ich wieder auf deine Komandos.", output='speech')
		luna.say(f"Die Hotworddetection wurde im Raum {room} eingeschaltet.", output='telegram')
	elif 'stopp' in text:
		luna.change_hotworddetection(room=room, changing_to='off')
		luna.say("Die Hotworddetection wurde ausgeschaltet, ab jetzt höre ich nicht mehr auf deine Komandos.", output='speech')
		luna.say(f"Die Hotworddetection wurde im Raum {room} ausgeschaltet, ab jetzt höre ich nicht mehr auf deine Komandos.", output='telegram')
		

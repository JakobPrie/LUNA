import os
import tempfile
import subprocess
import re 


def isValid(text):
	text = text.lower()
	if 'fehler' in text and ('senden' in text or 'schicken' in text):
		return True
	elif 'fehlermeldung' in text:
		return True
	
	
def handle(text, luna, profile):
	luna.say("Wilkommen in dem Modul, um einen Fehler zu senden. Wenn du nicht mehr weiter machen möchtest, dann sag einfach 'abbruch'.")
	luna.say("Bitte nenn deinen Namen.")
	name = luna.listen()
	if name is 'abbruch':
		name = 'UNDO'
		luna.say('Alles klar, der Vorgang wird abgebrochen!')
	else:
		luna.say("Alles klar, {}. Anschließend nenn bitte in einem Schlagwort den Anwendungsbereich ".format(name))
		modul_name = luna.listen()
		if modul_name is 'abbruch':
			modul_name = 'UNDO'
			luna.say('Alles klar, der Vorgang wird abgebrochen!')
		else:
			luna.say('Bitte nenn deine E-Mail-Adresse oder eine andere Möglichkeit, wie man dich erreichen kann.')
			mail = luna.listen()
			if mail is 'abbruch':
				mail = 'UNDO'
				luna.say('Alles klar, der Vorgang wird abgebrochen!')
			else:
				luna.say("Okay gut. Nun beschreib den Fehler bitte ausführlicher. Ab jetzt kannst du leider den Vorgang nicht mehr abbrechen. ")
				description = luna.listen()			
			
			
			sendIssu(name, modul_name, mail, description)
			luna.say('Vielen Dank! Ich werde den Fehler an Jakob weiterleiten. Bitte schick auch in Zukunft Fehler, damit Luna weiterhin gut genutzt werden kann.')
			luna.end_Conversation()

def sendIssu(name, modul_name, mail, description):
	from simplemail import Email
	Email(
		from_address = "luna_issus@outlook.de",
		to_address = "jakob.priesner@outlook.de",
		subject = "LUNA - Fehler!",
		message = "Name: {}\nModul-Name: {}\nMail: {}\nNachricht: {}".format(name, modul_name, mail, description)
	).send()

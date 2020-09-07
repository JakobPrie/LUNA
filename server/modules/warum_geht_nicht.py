

def isValid(text):
	text = text.lower()
	if 'warum' in text and ('funktioniert' in text or 'geht' in text) and 'nicht' in text:
		return True
		

def handle(text, luna, profile):
	text = text.lower()
	luna.say('Tut mir leid, dieses Modul ist noch in der Entwicklung. Bitte versuche es später erneut.')

def in_progress(text, luna, profile):
	if 'einkaufsliste' in text:
		luna.say('Die Einkaufsliste trennt die einzelnen Items bei jedem und. Daher musst du diese auch mit und trennen, ansonsten werden diese zusammengezogen. ')
		luna.say('Versuch doch mal folgende Syntax: Luna, setz Butter und 500g Rinderhack und Marmelade auf die Einkaufsliste.')

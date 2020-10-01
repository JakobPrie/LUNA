import time

SECURE = False

def isValid(text):
    text = text.lower()
    if 'lade' in text and 'nutzer' in text and 'neu' in text:
        return True
    else:
        return False

def handle(text, luna, profile):
    luna.asynchronous_say('Okay, warte einen Moment')
    # Einfach der Nutzer-Klasse den Laden-Befehl geben...
    luna.Users.load_users()
    time.sleep(1)
    print('--------- FERTIG ---------\n\n')
    luna.say('Die Nutzer wurden neu geladen.')

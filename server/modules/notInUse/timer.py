
def isValid(text):
    if 'timer' in text:
        return True

def handle(text, luna, profile):
    text = text.lower()
    if 'starte' in text or 'stoppe' in text:
        luna.say('Bist du dir sicher, dass du den Teimer und nicht die Stoppuhr meinst?')
    else:
        text = 'Timer abgelaufen.'
        if 'essen' in text:
            text = 'Guck doch mal nach deinem Essen.'
        E_eins = {'Zeit': luna.analysis['datetime'], 'Text': text, 'Benutzer': luna.user}
        if 'timer' in luna.local_storage.keys():
            luna.local_storage['timer'].append(E_eins)
        else:
            luna.local_storage['timer'] = [E_eins]


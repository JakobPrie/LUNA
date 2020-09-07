SECURE = False

def isValid(text):
    text = text.lower()
    if 'präsentation' in text and 'modus' in text:
        return True

def handle(text, luna, profile):
    if luna.core.presentation_mode == True:
        luna.core.presentation_mode = False
        luna.say('In Ordnung, der Präsentationsmodus ist beendet.')
    else:
        luna.core.presentation_mode = True
        luna.say('Alles klar, der Präsentationsmodus ist gestartet.')

PRIORITY = -1
SECURE = True

def isValid(text):
    text = text.lower()
    if ('was' in text or 'wie' in text) and 'die antwort' in text:
        return True


def handle(text, luna, profile):
    luna.say('42')

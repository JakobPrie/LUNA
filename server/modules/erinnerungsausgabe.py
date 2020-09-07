SECURE = True # Damit es von fortlaufenden module naufgerufen werden kann

def handle(text, luna, profile):
    user = text.get('Benutzer')
    tx = text.get('Text')
    luna.say(tx, user=user)

def isValid(txt):
    return False

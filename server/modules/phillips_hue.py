

def isValid(text):
    """
    text = text.lower()
    colors = ['blau', 'rot', 'gelb', 'grün', 'pink', 'lila', 'türkis', 'weiß', 'dunkelgrün', 'braun', 'orange', 'warmweiß']
    if ('mach' in text or 'licht' in text) and ('an' in text or 'aus' in text or 'heller' in text or 'dunkler' in text):
        return True
    for item in colors:
        if item in text and 'licht' in text:
            return True
    """
    return False
    
def handle(text, luna, profile):
    room = luna.analysis["room"]
    print(room)
    if room is 'NONE':
        luna.say('Du musst einen Raum angeben, wenn du mir diesen Befehl über Telegram schickst!', output='telegram')
    else:
        luna.start_module(user=luna.user, name='phillips_hue', text=text, room=room)


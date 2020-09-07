import re

# Beschreibung
'''
Mit diesem Modul kann man sich Nachrichten per Telegram zuschicken lassen.
Dazu sagt man "Sende <text> an mein Smartphone" oder "Smartphone Nachricht <text>".
'''

SECURE = False # Nicht SECURE, da Nachrichten an Telegram bei einer Verbindung per WebSocket
               # nicht speziell behandelt werden. Deshalb macht das keinen Sinn.

def isValid(text):
    text = text.lower()
    if 'smartphone' in text and ('nachricht' in text or 'sende' in text):
        return True
    else:
        return False

def get_aussage_gemeinsam():
    
    liste = luna.local_storage.get('einkaufsliste')
    i = 0
    aussage = ''
    while i < len(liste) - 1:
        if i != 0:
            aussage = aussage + ', ' + liste[i]
            i += 1
        else:
            aussage = liste[i]
            
    aussage = aussage + ' und ' + liste[len(liste)]
    return aussage

def handle(text, luna, local_storage):
    text = text.lower()
    length = len(text)
    
    if 'einkaufsliste' in text:
        if 'gemeinsam' in text or 'gemeinsame' in text:
            luna.say(get_aussage_gemeinsam(txt, luna), output='telegram')
        else:
            luna.say(get_aussage(txt, luna), output='telegram')
    else:
        match = re.search('^smartphone nachricht', text)
        if match != None:
            end = match.end() + 1
            nachricht = text[end:length]

        else:
            liste = re.split('\s', text)
            elements = len(liste)
            if liste[0] == 'sende' and liste[elements-1] == 'smartphone':
                nachricht = ''
                for i in range(1,elements):
                    if liste[i] == 'an' and liste[i+1] == 'mein':
                        break
                    else:
                        nachricht += liste[i]
                        nachricht += ' '

        if nachricht != '':
            if luna.telegram_call:
                luna.say('Du hast folgende Nachricht an dich selbst geschrieben:')
            else:
                luna.say("Ok, ich sende " + nachricht + " an dein Smartphone")
                luna.say("Nachricht an dich:", output='telegram')
            luna.say(nachricht, output='telegram')
        else:
            luna.say("Ich konnte deine Nachricht nicht heraus filtern")

import random

# Beschreibung
'''
In diesem Spiel geht es darum, eine Zufallszahl in möglichst wenigen Schritten zu erraten.
'''

SECURE = True

def isValid(text):
    text = text.lower()
    if 'spiel' in text and ('zahl' in text or 'erraten' in text):
        return True
    else:
        return False

def handle(text, luna, local_storage):
    if luna.telegram_call:
        zahl = random.randrange(1000)
        tipp = 0
        i = 0

        luna.say('Ok, lasse uns spielen. Versuche die Zufallszahl in möglichst wenigen Schritten zu erraten')

        while tipp != zahl:
            luna.say('Dein Tipp:')
            tipp = int(luna.listen())

            if zahl < tipp:
                luna.say("Die gesuchte Zahl ist kleiner als " + str(tipp))
            if zahl > tipp:
                luna.say("Die gesuchte Zahl ist größer als " + str(tipp))
            i += 1

        luna.say("Du hast die Zahl beim " + str(i) + ". Tipp erraten! SUPER!")

    else:
        luna.say('Das Spiel kann leider nur über Telegram gespielt werden')

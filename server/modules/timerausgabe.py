import os
import time

SECURE = True  # Damit es von fortlaufenden module naufgerufen werden kann


def handle(text, luna, profile):
    user = text.get('Benutzer')
    to_say = text.get('Text')
    duration = text.get('Dauer')

    luna.say("Dein Timer von {} ist abgelaufen!".format(duration))
    if not luna.telegram_call:
        luna.say("Dein Timer von {} ist abgelaufen!".format(duration), output='telegram')


def isValid(text):
    return False

import os

SECURE = True # Damit es von fortlaufenden module naufgerufen werden kann

def handle(text, luna, profile):
    user = text.get('Benutzer')
    to_say = text.get('Text')
    ton = text.get('Ton')
    path = luna.path + "/modules/resources/Weckertöne/" + ton
    
    if luna.local_storage['module_storage']['phillips_hue']['Bridge-IP'] != '':
        luna.start_module(user=text['Benutzer'], name='phillips_hue', text='Mach das Licht weiß')
    luna.play(path=path)

def isValid(text):
    return False

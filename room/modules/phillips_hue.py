from typing import List, Any
import random
from phue import Bridge
from rgbxy import Converter
import time


colors = ['blau', 'rot', 'gelb', 'grün', 'pink', 'lila', 'türkis', 'weiß', 'orange', 'warmweiß']
#code = ['0000ff', 'ff0000', 'ffff00', '00FF00', 'ff1493', '9400d3', '00ffff', 'ffffff', '006400', '8b4513', 'ff8c00',
#        'F5DA81']
code = [[0.1548, 0.1117], [0.6778, 0.3017], [0.439, 0.4446], [0.2015, 0.6763], [0.5623, 0.2457], [0.2398, 0.1197], [0.1581, 0.2367], [0.3146, 0.3304], [0.588, 0.386], [0.4689, 0.4124]]
light_names = []
regenbogenfarbe_ongoing = False

def isValid(text):
    text = text.lower()
    if ('mach' in text or 'licht' in text) and ('an' in text or 'aus' in text or 'hell' in text or 'heller' in text or 'dunkler' in text or 'prozent' in text or '%' in text):
        return True
    #elif 'regenbogen' in text and 'licht' in text:
    #    return True
    else:
        for item in colors:
            if item in text and 'licht' in text:
                return True


def handle(text, luna, profile):
    ip = luna.module_storage(module_name="phillips_hue").get("Bridge-IP")
    bridge = Bridge(ip)

    text = text.lower()
    
    for l in bridge.lights:
        light_names.append(l.name)
    print('Lichtnamen: {}'.format(light_names))
    lights = []
    
    # it is assumed that the LUNA room names are identical to the names of the pHUE rooms
    room = get_room(luna)
    room_lights = bridge.get_group(room, 'lights')
    print('Alle Lichter im Raum: {}'.format(room_lights))
    
    """
    for item in room_lights:
        room_lights.append(int(item))
    print('Room_lights: {}'.format(room_lights))
    """
    
    light = get_lights(luna, text)
    if light[0] is not 'FALSE':
        lights = light
    else:
        for item in room_lights:
            lights.append(item)
            lights.append(int(item))
    if room is 'FALSE':
        luna.say('Du musst einen Raum angeben, wenn du mir diesen Befehl über Telegram schickst!')
    else:
        Wrapper(bridge, lights, text, luna)


def Wrapper(bridge, lights, text, luna):
    if 'aus' in text:
        print('aus')
        light_off(bridge, lights)

    elif 'an' in text:
        light_on(bridge, lights)

    elif 'heller' in text:
        if 'viel' in text:
            light_brighter(bridge, lights, 140, luna)
        else:
            light_brighter(bridge, lights, 60, luna)

    elif 'dunkler' in text or 'dimm' in text:
        if 'viel' in text:
            light_darker(bridge, lights, 140, luna)
        else:
            light_darker(bridge, lights, 60, luna)
    
    elif 'hell' in text:
        light_set_brightsness(bridge, lights, 254)
    
    elif 'prozent' in text or '%' in text:
        light_set_brightsness(bridge, lights, get_brightness(text, luna))
    
    for item in colors:
        if item in text:
            light_change_color(bridge, lights, luna, text)
    
    #elif 'regenbogen' in text and 'licht' in text:
    #    regenbogenfarbe(bridge, lights, luna)
    #else:
    #    luna.say('Leider habe ich nicht verstanden, was ich mit dem Licht machen soll.')

def light_on(bridge, lights):
    #print(lights)
    bridge.set_light(lights, 'on', True)
    bridge.set_light(lights, 'bri', 254)
    print('Licht eingeschaltet')

def light_off(bridge, lights):
    #print(lights)
    bridge.set_light(lights, 'on', False)
    print('Licht ausgeschaltet')

def light_change_color(bridge, lights, luna, text):
    color = get_color(text, luna)
    if color[0] != -1 and color[1] != -1:
        light_on(bridge, lights)
        bridge.set_light(lights, 'xy', [color[0], color[1]])
        bridge.set_light(lights, 'bri', 254)
        print('Farbe geändert')
    else:
        luna.say('Es tut mir leid, leider konnte ich nicht heraus filtern, welche Farbe du wünschst.')

"""
def regenbogenfarbe(bridge, lights, luna):
    regenbogenfarbe_ongoing = True
    while regenbogenfarbe_ongoing is True:
        i = 0
        for item in lights:
            color = code[i]
            bridge.set_light(lights, 'xy', color)
            if i >= len(code): #>= an sich unnötig, allerdings zum Vorbeugen eines Fehlers sinvoll
                i = 0
            else:
                i += 1
            time.sleep(1)
"""

# lamp_brighter and lamp_darker are realy redundant...
def light_brighter(bridge, lights, value, luna):
    try:
        for item in lights:
            brightness = bridge.get_light(int(item), 'bri') + value
            # then a faulty return value should simply be avoided
            if brightness > 254:
                brightness = 254
            if brightness < 0:
                brightness = 0
            bridge.set_light(item, 'bri', brightness)
    except:
        #'Try and catch' are unnecessary, since the <0 and >254 actually exclude any incorrect value, but I would rather be on the safe side here
        luna.say(random.choice[
                     'Tut mir leid, leider konnte ich die Helligkeit nicht erhöhen.', 'Anscheinend habe ich einen Rechenfehler gemacht. Bitte gib mir doch noch eine zweite Möglichkeit.', 'Leider habe ich es nicht geschafft, das Licht zu dimmen. Da hat Jakob bein Programmieren wohl was verkackt.'])
        
def light_darker(bridge, lights, value, luna):
    try:
        for item in lights:
            brightness = bridge.get_light(int(item), 'bri') - value
            # then a faulty return value should simply be avoided
            if brightness > 254:
                brightness = 254
            if brightness < 0:
                brightness = 0
            bridge.set_light(item, 'bri', brightness)
    except:
        #'Try and except' are unnecessary, since the <0 and >254 actually exclude any incorrect value, but I would rather be on the safe side here
        luna.say(random.choice['Tut mir leid, leider konnte ich die Helligkeit nicht erhöhen.', 'Anscheinend habe ich einen Rechenfehler gemacht. Bitte gib mir doch noch eine zweite Möglichkeit.', 'Leider habe ich es nicht geschafft, das Licht zu dimmen. Da hat Jakob bein Programmieren wohl was verkackt.'])

def light_set_brightsness(bridge, lights, value):
    bridge.set_light(lights, 'bri', value)

def get_room(luna):
    room = luna.analysis["room"]
    if room == None:
        if luna.room_name == 'telegram':
            room = 'FALSE'
        else:
            room = luna.room_name
    return room

def get_lights(luna, text):
    # afterwards it is checked, whether only certain lamps should be addressed or all shoud be changed
    lights = ['FALSE']
    for item in light_names:
        if item in text:
            lights.append(item)
    return lights

def get_color(text, luna):
    converter = Converter()
    color = [-1, -1]
    founded = 0
    for item in range(len(colors)):
        if colors[item] in text:
            farbe = code[item]
            # folgende 2 Zeilen werden nur dann verwendet, wenn man die Farben als hex-Code angibt
            #color[0] = converter.hex_to_xy(farbe)[0]
            #color[1] = converter.hex_to_xy(farbe)[1]
            color[0] = code[item][0]
            color[1] = code[item][1]
            founded += 1

    if founded > 1:
        luna.say(
            'Du hast mehr als eine Farbe genannt. Dies kann ich leider nicht umsetzten und werde daher die letzte, die du genannt hast, nehmen.')

    return color


def get_brightness(text, luna):
    brightness = -1
    text = text.replace('prozent', '%') # unnötig, da sowieso wegen der SpeechRecognition % aber sicher ist sicher
    text_split = text.split(' ')
    for item in range(len(text_split)):
        if '%' in text_split[item]:
            prozent = text_split[item]
            prozent = prozent.replace('%', '')
            prozent = int(prozent) /100 *254
            brightness = int(prozent)
    return brightness


def change_brightness(bridge, text, value, luna):
    brightness = [-1]
    i = 0
    if 'alle' in text:
        room = getRoom()
        for light in room:
            brightness[i] = bridge.get_light(light, 'bri')
            i += 1
    else:
        brightness[i] = bridge.get_light(getLampName(text), 'bri')

    if 'heller' in text:
        for item in brightness:
            brightness[item] += value
    elif 'dunkler' in text or 'dimm' in text:
        for item in brightness:
            brightness[item] -= value

    # anschließend soll einfach zur Sicherheit ein fehlerhafter Rückgabewert vermieden werden
    if brightness > 254:
        brightness = 254
    if brightness < 0:
        brightness = 0

    return brightness

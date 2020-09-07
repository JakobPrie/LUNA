import time

SECURE = False

def reload_own(luna):
    print('\n\n--------- RELOAD ---------')
    # Eigene Module neu laden
    luna.core.Modules.stop_continuous()
    luna.core.Modules.load_modules()
    luna.core.Modules.start_continuous()

def handle(text, luna, profile):
    luna.asynchronous_say('Okay, warte einen Moment')
    rooms_counter = 0
    reloaded = False

    if 'server' in text.lower() or luna.server_name in text.lower():
        reload_own(luna)
        reloaded = True
    elif luna.analysis['room'] is not None:
        # Befehl nur an einen bestimmten Raum senden
        luna.rooms[luna.analysis['room']].Clientconnection.send({'LUNA_reload_modules':True})
        rooms_counter += 1
    else:
        # Befehl an alle Räume senden
        for room in luna.rooms.values():
            room.Clientconnection.send({'LUNA_reload_modules':True})
            rooms_counter += 1
        reload_own(luna)
        reloaded = True

    # Warten, bis die Räume fertig sind
    while rooms_counter > 0:
        for room in luna.rooms.values():
            response = room.Clientconnection.readanddelete('LUNA_confirm_reload_modules')
            if response is not None:
                if response == True:
                    rooms_counter -= 1
    if reloaded:
        time.sleep(1)
        print('--------- FERTIG ---------\n\n')
    luna.say('Die Module wurden neu geladen.')


def isValid(text):
    text = text.lower()
    if 'lad' in text and 'module' in text:
        return True
    else:
        return False

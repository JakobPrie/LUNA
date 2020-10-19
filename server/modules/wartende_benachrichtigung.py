SECURE = True


def isValid(text):
    return False


def handle(text, luna, profile):
    print("wartende benachrichtigungen")
    infos = luna.local_storage["users"][luna.user]["wartende_benachrichtigungen"]
    if len(infos) >= 1:
        if len(infos) > 1:
            text = "Hier noch ein paar wichtige Nachrichten für dich:"
        else:
            text = "Hier noch eine wichtige Nachricht für dich:"

        luna.say(text)
        for item in infos:
            # Es wird auch überprüft, ob die Benachrichtigung eventuell eine Audio ist, oder nicht
            if item.startswith("\Audio:"):
                luna.play(pfad=item.remove("\Audio:"))
            else:
                luna.say(item)
            luna.local_storage["users"][luna.user]["wartende_benachrichtigungen"].remove(item)

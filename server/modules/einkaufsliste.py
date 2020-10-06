import traceback
import random
from module_skills import assamble_array, get_enumerate, get_text_beetween

# Priorität gesetzt, da ansonsten manchmal das modul reload_modules.py aufgerufen wurde.
PRIORITY = 2
SECURE = True


def isValid(text):
    text = text.lower()
    if 'to' in text and 'do' in text and 'liste' in text:
            return False
    if 'einkaufsliste' in text:
        if 'setz' in text or 'setzte' in text or 'schreib' in text or 'schreibe' in text or 'füg' in text or 'füge' in text:
            return True
        elif ('was' in text and 'steht' in text and 'auf' in text) or ('gib' in text and 'aus' in text):
            return True
        elif ('lösch' in text or 'leere' in text) and 'einkaufsliste' in text:
            return True
        elif ('send' in text or 'schick' in text or 'schreib' in text):
            return True
        elif 'räum' in text and 'auf' in text:
            return True
    else:
        return False
        

def get_item(text, luna):
    text = luna.text
    # Man könnte meinen, dass text.lower() hier sinnvoller wäre, allerdings würden dann die Namen
    # der Items, die auf die Liste gesetzt werden sollen auch in Kleinbuchstaben gespeichert werden
    # würden. Das ganze im Nachhinein zu regeln wäre viel zu umständlich
    text = text.replace('Und',
                        'und')  # einfach nur zur Sicherheit, damit die Item-Trennung später auch sicher funktioniert
    text = text.replace(' g ', 'g ')
    text = text.replace(' gram ', 'g ')
    text = text.replace(' kg ', 'kg ')
    text = text.replace(' kilogram ', 'kg ')
    text = text.replace('eine ', '')
    text = text.replace('einen ', '')
    text = text.replace('ein ', '')
    item = []
    index = 0

    # es wird ermittel, wo die Nennung der items beginnt und wo sie endet
    if 'setz auf die einkaufsliste ' in text:
        text.replace('setz auf die Einkaufsliste ', (''))
        text = text.split(' ')
        index = 0
    # Anschließend werden der index, etc. herausgefunden
    elif 'setz' in text or 'setzte' in text or 'schreib' in text or 'schreibe' in text:
        text = text.split(' ')
        founded = False
        i = 0
        while i <= len(text) and founded is False:
            if text[i] == 'setz' or text[i] == 'setzte' or text[i] == 'schreib' or text[i] == 'schreibe':
                index = i + 1
                founded = True
            i += 1

    elif 'füg' in text or 'füge' in text:
        text = text.split(' ')
        founded = False
        i = 0
        while i <= len(text) and founded is False:
            if text[i] == 'füg' or text[i] == 'füge':
                index = i + 1
                founded = True
            i += 1

    elif 'lösch' in text:
        text = text.split(' ')
        founded = False
        i = 0
        while i <= len(text) and founded is False:
            if text[i] == 'lösch' or text[i] == 'lösche':
                index = i + 1
                founded = True
            i += 1
    # Wenn kein Index gefunden wurde, sagt Luna das
    else:
        index = -1
        luna.say('Ich habe leider nicht verstanden, was ich auf die Liste setzen soll. ')

    """
    Dieser Algorithmus trennt nicht die genannten Items nach dem Wort 'und', sondern filtert sie heraus. Probleme gibt es hier nur, wenn
    ein item aus mehreren Wörtern besteht, wie zum Beispiel 'Creme legere'
    #text = text.replace('und', '')
    if index != -1:
        stop = False
        point = index
        while stop is False:
            if text[point] is 'auf' or text[point] is 'zu' or text[point] is 'zur':
                stop = True
            elif text[point + 1] is 'g' or text[point + 1] is 'kilo':
                item.append(text[point] + ' ' + text[point + 1] + ' ' + text[point + 2])
                point += 2
            elif text[point] is 'ein' or text[point] is 'einen' or text[point] is 'eine' or text[point] is 'zwei' or \
                    text[point] is 'drei' or text[point] is 'vier' or text[point] is 'fünf' or text[point] is 'sechs' or \
                    text[point] is 'sieben' or text[point] is 'acht' or text[point] is 'neun' or text[point] is 'zehn':
                item.append(text[point] + ' ' + text[point + 1])
                point += 1
            elif text[point] is 'und':
                continue
            else:
                item.append(text[point])
            point += 1
    """

    # Der folgende Alorithmus trennt die genannten Items ganz stumpf bei jedem 'und'
    if index != -1:
        aussage_item = ''
        position = index
        stop = False
        while stop == False:
            if text[position] == 'auf' or text[position] == 'zu' or text[position] == 'zur' or text[
                position] == 'aus' or text[position] == 'von':

                item.append(aussage_item.strip())
                stop = True
            elif text[position] == 'und':
                item.append(aussage_item.strip())
                aussage_item = ''
            else:
                aussage_item += text[position] + ' '

            position += 1
    # ... und zählt alle Dopplungen zusammen
    duplicates_in_items = [item[i] for i in range(len(item)) if not i == item.index(item[i])]
    # anschließend werden Dopplungen, die durch die letzte Zeile entstehen könnten gelöscht
    if duplicates_in_items:
        item = assamble_array(item)
    return item

# ToDO: Die folgende Funktion ist unnötig, das kann man auch im Benutzungsfall einfügen
def get_aussage_gemeinsam(text, luna):
    aussage = ''
    if 'einkaufsliste' in luna.local_storage.keys():
        einkaufsliste = luna.local_storage.get('einkaufsliste')
        aussage = get_enumerate(einkaufsliste)
    return aussage

# ToDO: Die folgende Funktion ist unnötig, das kann man auch im Benutzungsfall einfügen
def get_aussage(text, luna):
    nutzer = luna.user
    nutzerdictionary = luna.local_storage.get('users')
    nd = nutzerdictionary.get(nutzer)
    aussage = ''
    if 'einkaufsliste' in nd.keys():
        einkaufsliste = nd['einkaufsliste']
        aussage = get_enumerate(einkaufsliste)

    return aussage


def handle(text, luna, profile):
    text = text.lower()
    text = text.replace('setze', ('setz'))

    if 'setz' in text or 'schreib' in text or 'füg' in text:
        item = get_item(text, luna)
        own_list = False
        # anschließend wird unterscheidet, ob die eigene oder gemeinsame Einkaufsliste benötigt wird
        if 'eigene' in text or 'meine' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'einkaufsliste' not in nd.keys():
                nd['einkaufsliste'] = []
            einkaufsliste = nd['einkaufsliste']
            own_list = True
        else:
            if 'einkaufsliste' not in luna.local_storage.keys():
                luna.local_storage['einkaufsliste'] = []
            einkaufsliste = luna.local_storage['einkaufsliste']
        if einkaufsliste:
            # Nur wenn die Einkaufsliste schon vorhanden ist...
            double_items = get_double_items(item, einkaufsliste, luna)
            if double_items:
                # Es gibt Dopplungen! Das darf nicht sein...
                # Wir fragen mal nach, ob die Dopplungen gewollt sind, oder eher nicht
                # Im selben Zug passen wir nur noch die Aussage an Singular und Plural an
                if len(double_items) > 1:
                    luna.say(
                        '{} befinden sich bereits auf der einkaufsliste. Soll ich sie dennoch auf die Einkaufsliste setzen?'.format(
                            get_enumerate(double_items)))
                else:
                    luna.say(
                        '{} befindet sich bereits auf der einkaufsliste. Soll ich sie dennoch auf die Einkaufsliste setzen?'.format(
                            get_enumerate(double_items)))
                response = luna.listen()
                # Vlt möchte der User ja nur bestimmte Dopplungen behalten...
                if 'nur' in text and 'nicht' in text:
                    item.remove(get_item(get_text_beetween('nur', text, end_word='nicht', output='String')))
                # Oder halt alle...
                elif 'ja' in response or 'gerne' in response or 'bitte' in response:
                    for i in item:
                        einkaufsliste.append(i)
                    neue_einkaufsliste = assamble_array(einkaufsliste)
                    einkaufsliste = neue_einkaufsliste
                # Oder auch gar keine.
                else:
                    for i in double_items:
                        item.remove(i)
                    if not item:
                        luna.say('Alles klar, ich setze nichts auf die Einkaufsliste.')
                        pass
                    else:
                        for i in item:
                            einkaufsliste.append(i)
                        neue_einkaufsliste = assamble_array(einkaufsliste)
                        einkaufsliste = neue_einkaufsliste
                        luna.say('Alles klar, ich habe nur {} auf die Einkaufsliste gesetzt.'.format(
                            get_enumerate(item)))

            else:
                # Scheinbar gibt es keine Dopplungen, also werden einfach alle items auf die Liste gesetzt
                for i in item:
                    einkaufsliste.append(i)

        else:
            # Wenn die Einkaufsliste noch nicht vorhanden ist...
            einkaufsliste = []
            for i in item:
                einkaufsliste.append(i)
        # Bevor wir die Einkaufsliste so abspeichern, werden wir gleich auch noch die Dopplungen in der Liste, die durch
        # das Hinzufügen gerade enstanden sind, zusammenzählen.
        einkaufsliste = assamble_array(einkaufsliste)
        
        # Und noch die Liste im Local_storage, bzw. die des Nutzers aktualisieren
        if own_list:
            luna.say("Alles klar. Ich habe {} auf deine Einkaufsliste gesetzt.".format(get_enumerate(item)))
            nd['einkaufsliste'] = einkaufsliste
        else:
            luna.say("Alles klar. Ich habe {} auf die gemeinsame Einkaufsliste gesetzt.".format(get_enumerate(item)))
            luna.local_storage['einkaufsliste'] = einkaufsliste


    elif 'auf' in text and 'steht' in text and 'was' in text:
        # hier wäre die Unterscheidung zwischen eigener/gemeinsamer Unterscheidung vorab einfach nur unnötig, daher lassen wir das
        if 'meiner' in text or 'eigenen' in text:
            aussage = get_aussage(text, luna)
        else:
            aussage = get_aussage_gemeinsam(text, luna)
        # wenn man den Befehl über Telegram aufruft, macht die schick-Funktion mehr Sinn
        if luna.telegram_call:
            handle('schick einkaufsliste', luna, profile)
        else:
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich {}.'.format(aussage)
            else:
                ausgabe = 'Für dich steht aktuell nichts auf der Einkaufsliste.'
            luna.say(ausgabe)

    elif 'schick' in text and 'einkaufsliste' in text and 'und' in text and ('lösch' in text or 'leer' in text):
        # das elif beschreibt diesen Teil eigentlich schon sehr genau
        i = ''
        if 'meine' in text or 'eigene' in text:
            i = 'meine'
        else:
            i = 'gemeinsame'

        text = "schick {} einkaufsliste".format(i)
        handle(text, luna, profile)
        text = "leere {} einkaufsliste".format(i)
        handle(text, luna, profile)

    elif 'lösch' in text and ('aus' in text or 'von' in text) and 'einkaufsliste' in text:
        # einzelne items sollen auch gelöscht werden können
        items = get_item(text, luna)
        own_list = False
        if 'eigene' in text or 'meine' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'einkaufsliste' not in nd.keys():
                nd['einkaufsliste'] = []
                einkaufsliste = nd['einkaufsliste']
            own_list = True
        else:
            if 'einkaufsliste' not in luna.local_storage.keys():
                luna.local_storage['einkaufsliste'] = []
                einkaufsliste = luna.local_storage['einkaufsliste']

        if einkaufsliste:
            # Das selbe Procedere wie bei "setz auf die Einkaufsliste"
            deleted = []
            for item in items:
                try:
                    einkaufsliste.remove(item)
                    deleted.append(item)
                except:
                    traceback.print_exc()
                    luna.say(
                        'Scheinbar ist {} nicht in der Einkaufsliste vorhanden und konnte daher nicht gelöscht werden.'.format(
                            item))
                if len(deleted) != -1:
                    luna.say(get_enumerate(deleted) + ' wurde von deiner Einkaufsliste gelöscht.')
                else:
                    luna.say(
                        'Da ist wohl was schief gelaufe. Ich konnte leider nichts aus der Einkaufsliste löschen.')
        else:
            # Wenn die Einkaufsliste leer ist, können die zu löschenden Items gar nicht in der leeren Liste sein
            luna.say('Ich kann das leider nicht aus deiner Einkaufsliste löschen, da sie leer ist.')


    elif ('lösch' in text or 'leer' in text) and 'einkaufsliste' in text and not 'aus' in text:
        # Hier ist die ganze Einkaufsliste gemeint, daher ist das "and not 'aus'" sehr wichtig.
        # Man könnte sich überlegen, ob dieser Teil vlt in das letzte elif gehört
        word = 'geleert'
        if 'lösche' in text:
            word = 'gelöscht'

        if 'eigene' in text or 'meine' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'einkaufsliste' in nd.keys():
                empty = []
                nd['einkaufsliste'] = empty
                luna.say('Deine Einkaufsliste wurde {}.'.format(word))
            else:
                luna.say('Deine Einkaufsliste ist schon leer.')
        else:
            if 'einkaufsliste' in luna.local_storage:
                empty = []
                luna.local_storage['einkaufsliste'] = empty
                luna.say('Die Einkaufsliste wurde {}.'.format(word))
            else:
                luna.say('Die Einkaufliste ist schon leer.')

    elif 'send' in text or 'schick' in text or 'schreib' in text:
        # Hier soll die Einkaufsliste in einem ansprechenderem Design per Telegram geschickt werden
        user = ''
        if 'meine' in text or 'eigene' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            items = []
            if 'einkaufsliste' in nd.keys():
                user = luna.user + ' '
                items = nd['einkaufsliste']
            else:
                user = luna.user + ' '
        else:
            items = luna.local_storage.get('einkaufsliste')
        send_to_telegram(items, user, luna)

    elif 'räum' in text and 'auf' in text:
        # eigentlich sollte es nicht passieren, dass Sachen unordentlich
        # in der einkaufsliste stehen, aber sollte es doch sein, hat man
        # die möglichkeit manuell einzugreifen
        luna.say('Einen Moment bitte.')
        if 'meine' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            nd['einkaufsliste'] = assamble_array(nd['einkaufsliste'])
            luna.say('Deine Einkaufsliste wurde aufgeräumt!')
        else:
            luna.local_storage['einkaufsliste'] = assamble_array(luna.local_storage['einkaufsliste'])

            luna.say('Die Einkaufsliste wurde aufgeräumt!')


def send_to_telegram(items, user, luna):
    if items == None:
        items = []
    aussage = '--- Einkaufsliste: {}---\n'.format(user)
    for i in items:
        aussage = aussage + '- ' + i + '\n'
    aussage += '--------------------'
    luna.say(aussage, output='telegram')


def get_double_items(items, einkaufsliste, luna):
    double = []
    if einkaufsliste is None:
        double = []
    else:
        for item in items:
            anz = item.split(' ', 1)[0]
            try:
                anz = int(anz)
            except:
                pass
            if type(anz) is int:
                item = item.split(' ', 1)[1]
            if item in einkaufsliste:
                double.append(item)
    return double
    

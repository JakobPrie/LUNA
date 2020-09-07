

def isValid(text):
    text = text.lower()
    if 'setz' in text or 'setzte' in text or 'schreib' in text or 'schreibe' in text or 'füg' in text or 'füge' in text:
        return True
    elif ('was' in text and 'steht' in text and 'auf' in text) or ('gib' in text and 'aus' in text):
        return True
    elif ('lösch' in text or 'leere' in text) and 'to-do-liste' in text:
        return True
    elif ('send' in text or 'schick' in text or 'schreib' in text) and 'to-do-liste' in text:
        return True
        
def handle(text, luna, profile):
    text = text.lower()
    text = text.replace('setze', ('setz'))
    text = text.replace('todoliste' and 'to-doliste' and 'todo-liste', 'to-do-liste')
    if 'setz' in text or 'schreib' in text:
        item = get_item(text, luna)
        if 'eigene' in text or 'meine' in text:
            if text != '_UNDO_':
                ausgabe = ''
                nutzer = luna.user
                nutzerdictionary = luna.local_storage.get('users')
                nd = nutzerdictionary.get(nutzer)

                if 'toDo_liste' in nd.keys():
                    double_items = get_double_items(item, nd['toDo_liste'])
                    print('double Items: {}'.format(double_items))
                    if double_items:
                        print('Dopplungen gefunden')
                        luna.say(
                            'Folgende Items befinden sich bereits in deiner to-Do-Liste: {}. Soll ich sie dennoch auf die to-Do-Liste setzen?'.format(
                                luna.enumerate(double_items)))
                        response = luna.listen()
                        if 'ja' in response or 'gerne' in response:
                            for i in item:
                                nd['toDo_liste'].append(i)
                        else:
                            for i in double_items:
                                item.remove(i)
                            if not item:
                                # luna.say('Alles klar, ich setze nichts auf die to-Do-Liste.')
                                pass
                            else:
                                luna.say('Alles klar, nur {} wird auf die to-Do-Liste gesetzt.'.format(
                                    luna.enumerate(item)))
                                for i in item:
                                    nd['toDo_liste'].append(i)
                    else:
                        for i in item:
                            nd['toDo_liste'].append(i)


                else:
                    nd['toDo_liste'] = []
                    for i in item:
                        nd['toDo_liste'].append(i)

                ausgabe = random.choice(['In Ordnung, ich habe ' + luna.enumerate(item) + ' zu deiner to-Do-Liste hinzugefügt.',
                                         'Alles klar, ich habe ' + luna.enumerate(item) + ' auf deine to-Do-Liste gesetzt.',
                                         luna.enumerate(item) + ' zu deiner to-Do-Liste hinzugefügt.',
                                         'In Ordnung, {}, ich habe '.format(luna.user) + luna.enumerate(bitem) + ' auf deine to-Do-Liste gesetzt.'])
                if not item:
                    ausgabe = 'Ich habe nichts auf deine to-Do-Liste gesetzt.'
                luna.say(ausgabe)
        else:
            item = get_item(text, luna)
            print(item)
            if text != '_UNDO_':
                ausgabe = ''
                toDo_liste = {}
                if 'toDo_liste' in luna.local_storage.keys():
                    double_items = get_double_items(item, luna.local_storage['toDo_liste'])
                    print(double_items)
                    if double_items:
                        print('Dopplungen gefunden')
                        print(luna.enumerate(double_items))
                        luna.say(
                            'Folgende Items befinden sich bereits in der to-Do-Liste: {}. Soll ich sie dennoch auf die to-Do-Liste setzen?'.format(
                                luna.enumerate(double_items)))
                        response = luna.listen()
                        if 'ja' in response or 'gerne' in response:
                            for i in item:
                                luna.local_storage['toDo_liste'].append(i)
                        else:
                            for i in double_items:
                                item.remove(i)
                            for i in item:
                                luna.local_storage['toDo_liste'].append(i)
                    else:
                        for i in item:
                            luna.local_storage['toDo_liste'].append(i)

                else:
                    luna.local_storage['toDo_liste'] = []
                    for i in item:
                        luna.local_storage['toDo_liste'].append(i)

                ausgabe = random.choice(['In Ordnung, ich habe ' + luna.enumerate(item) + ' zur gemeinsamen to-Do-Liste hinzugefügt.',
                     'Alles klar, ich habe ' + luna.enumerate(item) + ' auf die gemeinsame to-Do-Liste gesetzt.',
                     'Alles klar, {}, ich habe '.format(luna.user) + luna.enumerate(
                         item) + ' zur gemeinsamen to-Do-Liste hinzugefügt.',
                     'In Ordnung, {}, ich habe '.format(luna.user) + luna.enumerate(
                         item) + ' auf die gemeinsame to-Do-Liste gesetzt.'])
                if not item:
                    ausgabe = 'Ich habe nichts auf die gemeinsame to-Do-Liste gesetzt.'
                luna.say(ausgabe)

    elif 'auf' in text and 'steht' in text and 'was' in text:
        if 'meiner' in text or 'eigenen' in text:
            aussage = get_aussage(text, luna)
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich {}, {}.'.format(aussage, luna.user)
            else:
                ausgabe = random.choice(['Für dich steht aktuell nichts auf der to-Do-Liste.',
                                         'Für dich steht aktuell nichts auf der to-Do-Liste, {}.'.format(luna.user),
                                         'Für dich steht gerade nichts auf der to-Do-Liste.',
                                         'Für dich steht gerade nichts auf der to-Do-Liste, {}.'.format(luna.user)])
            luna.say(ausgabe)
        else:
            aussage = get_aussage_gemeinsam(text, luna)
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich {}.'.format(aussage)
            else:
                ausgabe = random.choice(['Für dich steht aktuell nichts auf der to-Do-Liste.',
                                         'Für dich steht aktuell nichts auf der to-Do-Liste, {}.'.format(luna.user),
                                         'Für dich steht gerade nichts auf der to-Do-Liste.',
                                         'Für dich steht gerade nichts auf der to-Do-Liste, {}.'.format(luna.user)])
            luna.say(ausgabe)

    elif 'schick' in text and 'to-do-liste' in text and 'und' in text and ('lösch' in text or 'leer' in text):
        i = ''
        if 'meine' in text or 'eigene' in text:
            i = 'meine'
        else:
            i = 'gemeinsame'

        text = "schick {} to-do-liste".format(i)
        handle(text, luna, profile)
        text = "leere {} to-do-liste".format(i)
        handle(text, luna, profile)


    elif 'lösch' in text and ('aus' in text or 'von' in text) and 'to-do-liste' in text:
        items = get_item(text, luna)
        print(items)
        if 'meine' in text or 'eigene' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'toDo_liste' in nd.keys():
                toDo_liste = nd['toDo_liste']
                deleted = []
                for item in items:
                    try:
                        toDo_liste.remove(item)
                        deleted.append(item)
                    except:
                        traceback.print_exc()
                        luna.say(
                            'Scheinbar ist {} nicht in der to-Do-Liste vorhanden und konnte daher nicht gelöscht werden.'.format(
                                item))
                    if len(deleted) is not -1:
                        luna.say(luna.enumerate(deleted) + ' wurde von deiner to-Do-Liste gelöscht.')
                    else:
                        luna.say(
                            'Da ist wohl was schief gelaufe. Ich konnte leider nichts aus der to-Do-Liste löschen.')
            else:
                luna.say('Ich kann das leider nicht aus deiner to-Do-Liste löschen, da sie leer ist.')
        else:
            if 'toDo_liste' in luna.local_storage.keys():
                toDo_liste = luna.local_storage['toDo_liste']
                deleted = []
                for item in items:
                    try:
                        toDo_liste.remove(item)
                        deleted.append(item)
                    except:
                        traceback.print_exc()
                        luna.say(
                            'Scheinbar ist {} nicht in der to-Do-Liste vorhanden und konnte daher nicht gelöscht werden.'.format(
                                item))
                    if len(deleted) is not -1:
                        luna.say(luna.enumerate(deleted) + ' wurde von der gemeinsamen to-Do-Liste gelöscht.')
                    else:
                        luna.say(
                            'Da ist wohl was schief gelaufe. Ich konnte leider nichts aus der to-Do-Liste löschen.')
            else:
                luna.say('Ich kann das leider nicht aus deiner to-Do-Liste löschen, da sie leer ist.')


    elif ('lösche' in text or 'leere' in text) and 'to-do-liste' in text and not 'aus' in text:
        # print('lösche and to-do-liste in text')
        word = 'geleert'
        if 'lösche' in text:
            word = 'gelöscht'

        if 'eigene' in text or 'meine' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'toDo_liste' in nd.keys():
                empty = []
                nd['toDo_liste'] = empty
                luna.say('Deine to-Do-Liste wurde {}.'.format(word))
            else:
                luna.say('Deine to-Do-Liste ist schon leer.')
        else:
            if 'toDo_liste' in luna.local_storage:
                empty = []
                luna.local_storage['toDo_liste'] = empty
                luna.say('Die to-Do-Liste wurde {}.'.format(word))
            else:
                luna.say('Die Einkaufliste ist schon leer.')

    elif 'send' in text or 'schick' in text or 'schreib' in text:
        user = ''
        if 'meine' in text or 'eigene' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            items = []
            if 'toDo_liste' in nd.keys():
                user = luna.user + ' '
                items = nd['toDo_liste']
            else:
                user = luna.user + ' '
        else:
            items = luna.local_storage.get('toDo_liste')
        send_to_telegram(items, user, luna)       


def get_aussage_gemeinsam(text, luna):
    aussage = ''
    if 'toDo_liste' in luna.local_storage.keys():
        toDo_liste = luna.local_storage.get('toDo_liste')
        aussage = luna.enumerate(toDo_liste)
    return aussage

def get_aussage(text, luna):
    nutzer = luna.user
    nutzerdictionary = luna.local_storage.get('users')
    nd = nutzerdictionary.get(nutzer)
    # print(nd)
    aussage = ''
    if 'toDo_liste' in nd.keys():
        toDo_liste = nd['toDo_liste']
        aussage = luna.enumerate(toDo_liste)
    return aussage
    
def send_to_telegram(items, user, luna):
    if items == None:
        items = []
    print('Items: {}'.format(items))
    aussage = '--- to-Do-Liste: {}---\n'.format(user)
    for i in items:
        aussage = aussage + '- ' + i + '\n'
    aussage += '--------------------'
    luna.say(aussage, output='telegram')

def get_double_items(items, toDo_liste):
    double = []
    for item in items:
        if item in toDo_liste:
            double.append(item)
    return double

def get_item(text, luna):
    text = luna.text
    text = text.replace('Und',
                        'und')  # einfach nur zur Sicherheit, damit die Item-Trennung später auch sicher funktioniert
    text = text.replace(' g ', 'g ')
    text = text.replace(' gram ', 'g ')
    text = text.replace(' kg ', 'kg ')
    text = text.replace(' kilogram ', 'kg ')
    item = []
    index = 0

    # es wird ermittel, wo die Nennung der items beginnt und wo sie endet
    if 'setz auf die to-do-liste ' in text:
        text.replace('setz auf die to-Do-Liste ', (''))
        text = text.split(' ')
        index = 0

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
                print('index found')
                index = i + 1
                founded = True
            i += 1

    else:
        index = -1
        luna.say('Ich habe leider nicht verstanden, was ich auf die Liste setzen soll. '
                 'Versuch es doch Mal mit der Syntax: Setz Milch auf die Liste.')

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
    print('Index: {}'.format(index))
    # Der folgende Alorithmus trennt die genannten Items ganz stumpf bei jedem 'und'
    if index != -1:
        aussage_item = ''
        position = index
        stop = False
        # print('Länge: {}'.format(len(text)))
        while stop == False:
            # print('Position: {}, Text: {}'.format(position, text[position]))
            if text[position] == 'auf' or text[position] == 'zu' or text[position] == 'zur' or text[
                position] == 'aus' or text[position] == 'von':
                # print('stop = True')
                item.append(aussage_item)
                stop = True
            elif text[position] == 'und':
                # print('aussage wird zu item hinzugefügt')
                item.append(aussage_item)
                aussage_item = ''
            else:
                # print('aussage erweitert')
                aussage_item += text[position] + ' '

            # print()
            position += 1
    # print(item)
    return item

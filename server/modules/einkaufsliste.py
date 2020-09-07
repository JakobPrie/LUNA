
from module_skills import get_enumerate, delete_duplications, assamble_new_items
import traceback
import random
import traceback


# Priorität gesetzt, da ansonsten manchmal das modul reload_modules.py aufgerufen wurde.
PRIORITY = 2
SECURE = True


def get_item(text, luna):
    text = luna.text
    text = text.replace('Und', 'und') # einfach nur zur Sicherheit, damit die Item-Trennung später auch sicher funktioniert
    text = text.replace(' g ', 'g ')
    text = text.replace(' gram ', 'g ')
    text = text.replace(' kg ', 'kg ')
    text = text.replace(' kilogram ', 'kg ')
    item = []
    index = 0
    
    # es wird ermittel, wo die Nennung der items beginnt und wo sie endet
    if 'setz auf die einkaufsliste ' in text:
        text.replace('setz auf die Einkaufsliste ', (''))
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
        #print('Länge: {}'.format(len(text)))
        while stop == False:
            #print('Position: {}, Text: {}'.format(position, text[position]))
            if text[position] == 'auf' or text[position] == 'zu' or text[position] == 'zur' or text[position] == 'aus' or text[position] == 'von':
                #print('stop = True')
                item.append(aussage_item)
                stop = True
            elif text[position] == 'und':
                #print('aussage wird zu item hinzugefügt')
                item.append(aussage_item)
                aussage_item = ''
            else:
                #print('aussage erweitert')
                aussage_item += text[position] + ' '
            
            #print()
            position += 1
    #print(item)
    
    duplicates_in_items = [item[i] for i in range(len(item)) if not i == item.index(item[i])]
    if duplicates_in_items:
        luna.say('Du hast {} doppelt genannt. Soll ich deine doppelt genannten Sachen einfach zusammenzählen?'.format(get_enumerate(delete_duplications(duplicates_in_items))))
        response = luna.listen()
        if 'ja' in response:
            item = assamble_new_items(item, duplicates_in_items)
        else:
            item = delete_duplications(item)
    print('Item in get_item(): {}'.format(item))
    return item

def get_aussage_gemeinsam(text, luna):
    aussage = ''
    if 'einkaufsliste' in luna.local_storage.keys():
        einkaufsliste = luna.local_storage.get('einkaufsliste')
        aussage = get_enumerate(einkaufsliste)
    return aussage

def get_aussage(text, luna):
    nutzer = luna.user
    nutzerdictionary = luna.local_storage.get('users')
    nd = nutzerdictionary.get(nutzer)
    #print(nd)
    aussage = ''
    if 'einkaufsliste' in nd.keys():
        einkaufsliste = nd['einkaufsliste']
        aussage = get_enumerate(einkaufsliste)

    return aussage

def handle(text, luna, profile):
    text = text.lower()
    text = text.replace('setze', ('setz'))
    
    if 'setz' in text or 'schreib' in text:
        item = get_item(text, luna)
        if 'eigene' in text or 'meine' in text:
            if text != '_UNDO_':
                ausgabe = ''
                nutzer = luna.user
                nutzerdictionary = luna.local_storage.get('users')
                nd = nutzerdictionary.get(nutzer)

                if 'einkaufsliste' in nd.keys():
                    double_items = get_double_items(item, nd['einkaufsliste'], luna)
                    if double_items:
                        luna.say('Folgende Items befinden sich bereits in deiner Einkaufsliste: {}. Soll ich sie dennoch auf die Einkaufsliste setzen?'.format(get_enumerate(double_items)))
                        response = luna.listen()
                        if 'ja' in response or 'gerne' in response:
                            neue_einkaufsliste = assamble_new_items(nd['einkaufsliste'], item)
                            nd['einkaufsliste'] = neue_einkaufsliste
                        else:
                            for i in double_items:
                                item.remove(i)
                            if not item:
                                #luna.say('Alles klar, ich setze nichts auf die Einkaufsliste.')
                                pass
                            else:
                                neue_einkaufsliste = assamble_new_items(nd['einkaufsliste'], item)
                                nd['einkaufsliste'] = neue_einkaufsliste
                                luna.say('Alles klar, ich habe nur {} auf die Einkaufsliste gesetzt.'.format(get_enumerate(item)))

                    else:
                        for i in item:
                            nd['einkaufsliste'].append(i)
                                
                        
                else:
                    nd['einkaufsliste'] = []
                    for i in item:
                        nd['einkaufsliste'].append(i)
                
                ausgabe = random.choice(['In Ordnung, ich habe ' + get_enumerate(item) + ' zu deiner Einkaufsliste hinzugefügt.',
                                         'Alles klar, ich habe ' + get_enumerate(item) + ' auf deine Einkaufsliste gesetzt.',
                                         get_enumerate(item) + ' zu deiner Einkaufsliste hinzugefügt.',
                                         'In Ordnung, {}, ich habe {} auf deine Einkaufsliste gesetzt.'.format(luna.user, get_enumerate(item))])
                if not item:
                    ausgabe = 'Ich habe nichts auf deine Einkaufsliste gesetzt.'
                luna.say(ausgabe)
        else:
            print(item)
            if text != '_UNDO_':
                ausgabe = ''
                einkaufsliste = {}
                if 'einkaufsliste' in luna.local_storage.keys():
                    double_items = get_double_items(item, luna.local_storage['einkaufsliste'], luna)
                    if double_items:
                        luna.say('Folgende Items befinden sich bereits in der Einkaufsliste: {}. Soll ich sie dennoch manche auf die Einkaufsliste setzen?'.format(get_enumerate(double_items)))
                        response = luna.listen()
                        if 'ja' in response or 'gerne' in response:
                            neue_einkaufsliste = assamble_new_items(luna.local_storage['einkaufsliste'], item)
                            print(neue_einkaufsliste)
                            luna.local_storage['einkaufsliste'] = neue_einkaufsliste
                        else:
                            for i in double_items:
                                item.remove(i)
                            neue_einkaufsliste = assamble_new_items(luna.local_storage['einkaufsliste'], item)
                            print(neue_einkaufsliste)
                            luna.local_storage['einkaufsliste'] = neue_einkaufsliste
                    else:
                        print(item)
                        for i in item:
                            luna.local_storage['einkaufsliste'].append(i)
                            
                else:
                    luna.local_storage['einkaufsliste'] = []
                    for i in item:
                        luna.local_storage['einkaufsliste'].append(i)
                        
                ausgabe = random.choice(['In Ordnung, ich habe ' + get_enumerate(item) + ' zur gemeinsamen Einkaufsliste hinzugefügt.',
                                         'Alles klar, ich habe ' + get_enumerate(item) + ' auf die gemeinsame Einkaufsliste gesetzt.',
                                         'Alles klar, {}, ich habe '.format(luna.user) + get_enumerate(item) + ' zur gemeinsamen Einkaufsliste hinzugefügt.',
                                         'In Ordnung, {}, ich habe '.format(luna.user) + get_enumerate(item) + ' auf die gemeinsame Einkaufsliste gesetzt.'])
                if not item:
                    ausgabe = 'Ich habe nichts auf die gemeinsame Einkaufsliste gesetzt.'
                luna.say(ausgabe)

    elif 'auf' in text and 'steht' in text and 'was' in text:
        if 'meiner' in text or 'eigenen' in text:
            aussage = get_aussage(text, luna)
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich {}, {}.'.format(aussage, luna.user)
            else:
                ausgabe = random.choice(['Für dich steht aktuell nichts auf der Einkaufsliste.',
                                         'Für dich steht aktuell nichts auf der Einkaufsliste, {}.'.format(luna.user),
                                         'Für dich steht gerade nichts auf der Einkaufsliste.',
                                         'Für dich steht gerade nichts auf der Einkaufsliste, {}.'.format(luna.user)])
            luna.say(ausgabe)
        else:
            aussage = get_aussage_gemeinsam(text, luna)
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich {}.'.format(aussage)
            else:
                ausgabe = random.choice(['Für dich steht aktuell nichts auf der Einkaufsliste.',
                                         'Für dich steht aktuell nichts auf der Einkaufsliste, {}.'.format(luna.user),
                                         'Für dich steht gerade nichts auf der Einkaufsliste.',
                                         'Für dich steht gerade nichts auf der Einkaufsliste, {}.'.format(luna.user)])
            luna.say(ausgabe)
    
    elif 'schick' in text and 'einkaufsliste' in text and 'und' in text and ('lösch' in text or 'leer' in text):
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
        items = get_item(text, luna)
        print(items)
        if 'meine' in text or 'eigene' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'einkaufsliste' in nd.keys():
                einkaufsliste = nd['einkaufsliste']
                deleted = []
                for item in items:
                    try:
                        einkaufsliste.remove(item)
                        deleted.append(item)
                    except:
                        traceback.print_exc()
                        luna.say('Scheinbar ist {} nicht in der Einkaufsliste vorhanden und konnte daher nicht gelöscht werden.'.format(item))
                    if len(deleted) is not -1:
                        luna.say(get_enumerate(deleted) + ' wurde von deiner Einkaufsliste gelöscht.')
                    else:
                        luna.say('Da ist wohl was schief gelaufe. Ich konnte leider nichts aus der Einkaufsliste löschen.')
            else:
                luna.say('Ich kann das leider nicht aus deiner Einkaufsliste löschen, da sie leer ist.')
        else:
            if 'einkaufsliste' in luna.local_storage.keys():
                einkaufsliste = luna.local_storage['einkaufsliste']
                deleted = []
                for item in items:
                    try:
                        einkaufsliste.remove(item)
                        deleted.append(item)
                    except:
                        traceback.print_exc()
                        luna.say('Scheinbar ist {} nicht in der Einkaufsliste vorhanden und konnte daher nicht gelöscht werden.'.format(item))
                    if len(deleted) is not -1:
                        luna.say(get_enumerate(deleted) + ' wurde von der gemeinsamen Einkaufsliste gelöscht.')
                    else:
                        luna.say('Da ist wohl was schief gelaufe. Ich konnte leider nichts aus der Einkaufsliste löschen.')
            else:
                luna.say('Ich kann das leider nicht aus deiner Einkaufsliste löschen, da sie leer ist.')
        
    
    elif ('lösche' in text or 'leere' in text) and 'einkaufsliste' in text and not 'aus' in text:
        #print('lösche and einkaufsliste in text')      
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
    
    
def send_to_telegram(items, user, luna):
    if items == None:
        items = []
    print('Items: {}'.format(items))
    aussage = '--- Einkaufsliste: {}---\n'.format(user)
    for i in items:
        aussage = aussage + '- ' + i + '\n'
    aussage += '--------------------'
    luna.say(aussage, output='telegram')
         
def get_double_items(items, einkaufsliste, luna):
    double = []
    print(items)
    if einkaufsliste is None:
        double = []
    else:
        for item in items:
            anz = item.split(' ', 1)[0]
            if type(anz) is int:
                item = item.split(' ', 1)[1]
            if item in einkaufsliste:
                double.append(item)
    return double
            
def isValid(text):
    text = text.lower()
    if 'to' in text and 'do' in text and 'liste' in text:
        return False
    elif 'setz' in text or 'setzte' in text or 'schreib' in text or 'schreibe' in text or 'füg' in text or 'füge' in text:
        return True
    elif ('was' in text and 'steht' in text and 'auf' in text) or ('gib' in text and 'aus' in text):
        return True
    elif ('lösch' in text or 'leere' in text) and 'einkaufsliste' in text:
        return True
    elif ('send' in text or 'schick' in text or 'schreib' in text) and 'einkaufsliste' in text:
        return True
    

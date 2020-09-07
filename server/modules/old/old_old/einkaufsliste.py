import datetime
from datetime import date
import random

def get_item(txt, luna):
    item = ''
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    eingabe = tt.lower()
    satz = {}
    mind = 1 
    i = str.split(eingabe)
    ind = 1 
    for w in i:
        satz[ind] = w 
        ind += 1
    if 'setz' in eingabe and 'auf die' in eingabe:
        for iindex, word in satz.items():
            if word == 'setz' or word == 'setze':
                start = iindex
                for iindex, word in satz.items():
                    if iindex == start + mind:
                        if word != 'auf':
                            item = item + word + ' '
                            mind += 1
                        else:
                            break
    elif 'füg' in eingabe and 'zu' in eingabe:
        for iindex, word in satz.items():
            if word == 'füg' or word == 'füge':
                start = iindex
                for iindex, word in satz.items():
                    if iindex == start + mind:
                        if word != 'liste':
                            item = item + word + ' '
                            mind += 1
                        else:
                            h = str.split(item)
                            i = h[0:len(h)-1]
                            j = h[len(h)-1:]
                            if j == 'gemeinsamen':
                                i = i[0:len(h)-2]
                            else:
                                i = i
                            item = ''
                            for x in i:
                                item = item + str(x) + ' '
                            break
    else:
        item = item
    return item


def get_aussage(txt, luna): #Imperfection
    aussage = ''
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    eingabe = tt.lower()
    nutzer = luna.user
    usersdictionary = luna.local_storage.get('users')
    nutzerdictionary = usersdictionary.get(nutzer)
    
    '''
    if 'liste' in nutzerdictionary.keys():
        liste = nutzerdictionary.get('liste')
        i = 0
        if len(liste) > 1:
            while i < len(liste) - 1:
                aktuellesitem = liste[i]
                aussage = aussage + aktuellesitem + ', '
                i += 1
            aussage = aussage + ' und ' + liste[len(liste) - 1]
        else:
            while i < len(liste):
                aktuellesitem = liste[i]
                aussage = aussage + aktuellesitem + ', '
                i += 1
    else:
        aussage = ''
    '''
    
    if 'liste' in nutzerdictionary.keys():
        liste = nutzerdictionary.get('liste')
        i = 0
        while i < len(liste):
            aussage = aussage + ', ' + liste[i]
            i = i + 1
    else:
        aussage = '' 
        
    return aussage


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


def handle(txt, luna, profile):
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    text = tt.lower()
    
    if 'gemeinsame' in text and 'einkaufslsite' in text:
        if ('setze' in text or 'setz' in text) and 'auf' in text:
            item = get_item(text, luna)
            if text != '_UNDO_':
                ausgabe = ''
                einkaufslsite = {}
                if 'einkaufslsite' in luna.local_storage.keys():
                    luna.local_storage['einkaufsliste'].append(item)
                else:
                    luna.local_storage['einkaufsliste'] = item
                ausgabe = random.choice(['In Ordnung, ich habe ' + str(item) + 'zur gemeinsamen Liste hinzugefügt.', 'Alles klar, ich habe ' + str(item) + 'auf die gemeinsame Liste gesetzt.', 'Alles klar, {}, ich habe '.format(luna.user) + str(item) + 'zur gemeinsamen Liste hinzugefügt.', 'In Ordnung, {}, ich habe '.format(luna.user) + str(item) + 'auf die gemeinsame Liste gesetzt.']) #
                luna.say(ausgabe)
        elif 'steht' in text and 'auf' in text or 'was sagt die' in text or 'gibt' in text and 'auf' in text:
            aussage = get_aussage_gemeinsam(text, luna)
            if aussage != '':
                ausgabe = 'Auf der geimeinsamen Liste steht ' + aussage + ', {}.'.format(luna.user)
            else:
                ausgabe = random.choice(['Aktuell steht nichts auf der gemeinsamen Liste.', 'Aktuell steht nichts auf der gemeinsamen Liste, {}.'.format(luna.user), 'Gerade steht nichts auf der gemeinsamen Liste.', 'Gerade steht nichts auf der gemeinsamen Liste, {}.'.format(luna.user)])
            luna.say(ausgabe) 
    else:
        if 'setze' in text and 'auf die' in text or 'füge' in text and 'zu' in text:
            item = get_item(text, luna)
            if text != '_UNDO_':
                ausgabe = ''
                einkaufsliste = {}
                nutzer = luna.user
                nutzerdictionary = luna.local_storage.get('users')
                nd = nutzerdictionary.get(nutzer)
                if 'einkaufsliste' in nd.keys():
                    nd['einkaufsliste'].append(item)
                else:
                    nd['einkaufsliste'] = item
                ausgabe = random.choice(['In Ordnung, ich habe ' + str(item) + 'zur Liste hinzugefügt.', 'Alles klar, ich habe ' + str(item) + 'auf die Liste gesetzt.', 'Alles klar, {}, ich habe '.format(luna.user) + str(item) + 'zur Liste hinzugefügt.', 'In Ordnung, {}, ich habe '.format(luna.user) + str(item) + 'auf die Liste gesetzt.']) 
                luna.say(ausgabe)
        elif 'steht' in text and 'auf' in text or 'was sagt die' in text or 'gibt' in text and 'auf' in text:
            aussage = get_aussage(text, luna)
            if aussage != '':
                ausgabe = 'Auf der Liste steht für dich ' + aussage + ', {}.'.format(luna.user)
            else:
                ausgabe = random.choice(['Für dich steht aktuell nichts auf der Einkaufsiste.', 'Für dich steht aktuell nichts auf der Einkaufsliste, {}.'.format(luna.user), 'Für dich steht gerade nichts auf der Einkaufsliste.', 'Für dich steht gerade nichts auf der Einkaufsliste, {}.'.format(luna.user)])
            luna.say(ausgabe)


def isValid(txt):
    tt = txt.replace('.', (''))
    tt = tt.replace('?', (''))
    tt = tt.replace('!', (''))
    tt = tt.replace('.', (''))
    tt = tt.replace(',', (''))
    tt = tt.replace('"', (''))
    tt = tt.replace('(', (''))
    tt = tt.replace(')', (''))
    tt = tt.replace('â‚¬', ('Euro'))
    tt = tt.replace('%', ('Prozent'))
    tt = tt.replace('$', ('Dollar'))
    text = tt.lower()
    
    if ('setze' in text or 'setzt' in text) and 'auf' in text:
        return True
    elif 'steht' in text and 'auf' in text or 'was sagt die' in text or 'gibt' in text and 'auf' in text:
        return True    



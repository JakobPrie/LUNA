from time import sleep
import datetime

SECURE = True

def isValid(text):
    text = text.lower()
    if (text.startswith(
            'hallo') or text == 'hi' or text == 'hey' or text == '/start') and not 'geht' in text or 'läuft' in text:
        return True
    elif 'wie' in text and ('uhr' in text or 'spät' in text):
        return True
    elif 'welchen tag' in text or 'welcher tag' in text or 'wochentag' in text or 'datum' in text or 'den wievielten haben wir heute' in text or 'der wievielte ist es' in text:
        return True
    elif 'guten' in text and 'tag' in text:
        return True
    elif 'guten' in text and 'morgen' in text:
        return True
    elif 'guten' in text and 'abend' in text:
        return True
    elif 'gute' in text and 'nacht' in text:
        return True
    elif 'timer' in text or 'stoppuhr' in text or 'countdown' in text:
        return True
        
def handle(text, luna, profile):
    text = text.lower()
    now = datetime.datetime.now()
    wochentag = datetime.datetime.today().weekday()
    time = now.hour
    if ' uhr ' in text or 'spät' in text:
        luna.say('Es ist ' + get_time(now))
    elif 'welchen tag' in text or 'welcher tag' in text or 'wochentag' in text or 'datum' in text or 'den wievielten haben wir heute' in text or 'der wievielte ist es' in text:
        luna.say(get_day(text))
    elif 'hallo' in text:
        luna.say('Hallo, {}!'.format(luna.user))
    elif 'guten' in text and 'tag' in text:
        if time >= 20 and time <= 4:
            luna.say('Naja "Tag" würde ich das nicht mehr nennen, aber ich wünsche dir auch einen guten Abend')
        elif time >= 5 and time <= 20:
            luna.say('Guten Tag, {}'.format(luna.user))
    elif 'guten' in text and 'morgen' in text:
        if time is 4 or time is 5:
            luna.say('Hast du heute was wichtiges anstehen?')
            response = luna.listen
            if 'ja' in text:
                luna.say('Dann wünsche ich dir dabei viel Erfolg!')
            else:
                luna.say('Dann schlaf ruhig weiter, es ist noch viel zu früh, um aufzustehen.')
        elif time >= 6 and time<= 10:
            luna.say('Guten Morgen, {}'.format(luna.user))
        elif time is 11 or time is 12:
            luna.say('Wurde aber auch langsam Zeit, {}. Aber dennoch auch dir einen guten Morgen.'.format(luna.user))
        elif time >= 14 and time <= 18:
            luna.say(
                'Ob es noch Morgen ist, liegt wohl im Blickwinkel des Betrachters. Ich würde eher sagen, dass es Mittag oder Nachmittag ist.')
        elif time >= 19 and time <= 3:
            luna.say('Also Morgen ist es auf jeden Fall nicht mehr. Daher wünsche ich dir einfach Mal einen guten Abend.')
        else:
            luna.say('Hallo, {}'.format(luna.user))
    elif 'guten' in text and 'abend' in text:
        if time >= 6 and time <= 17:
            luna.say('Ob es noch Abend ist, liegt wohl im Blickwinkel des Betrachters. In Amerika ist es jetzt in der Tat Abend.')
        elif time >= 18 and time <= 5:
            luna.say('Gute nacht, {}'.foramt(luna.user))
        else:
            luna.say('Guten Abend, {}'.format(luna.user))

    elif 'gute' in text and 'nacht' in text:
        if time >= 1 and time <= 13:
            luna.say('Du solltest echt langsam ins Bett gehen.')
        elif time >= 8 and time <= 24 or time is 0:
            luna.say('Gute Nacht, {}.'.format(luna.user))
        else:
            luna.say('Eine sehr interessante Definition der derzeitigen Uhrzeit.')
        founded = False
        if 'Wecker' in luna.local_storage.keys():
            erinnerungen = luna.local_storage.get('Wecker')
            for item in erinnerungen:
                if item['Benutzer'] is luna.user:
                    founded = True
        if not founded:
            luna.say('Soll ich dich morgen wecken?')
            response = luna.listen()
            if 'ja' in response or 'gerne' in response or 'bitte' in response:
                if luna.analysis['datetime'] is None:
                    luna.say('Wann soll ich dich denn wecken?')
                    response_two = luna.listen()
                    text = 'weck ' + response_two
                    luna.start_module(text=text, user=luna.user)
                else:
                    luna.start_module(text=text, user=luna.user)
            else:
                luna.say('Okay, dann wünsche ich dir eine gute Nacht.')
    elif 'timer' in text:
        timer(text, luna)
    elif 'stoppuhr' in text:
        stopwatch(text, luna)
    elif 'counter' in text:
        counter(text, luna)
    else:
        luna.say('Aaahhh, das sind zu viele Möglichkeiten mit Zeiten umzugehen. Bitte versuche es erneut.')


def timer(text, luna):
    if 'start' in text or 'stopp' in text or 'beende' in text:
        luna.say('Sicher, dass du nicht die Stoppuhr meinst?')
        luna.say('Soll ich für dich eine Stoppuhr starten?')
        response = luna.listen()
        if 'ja' in response or 'bitte' in text or 'gerne' in text:
            luna.say('Okay, soll ich eine Stoppuhr nur für dich oder für alle starten?')
            response = luna.listen()
            if 'mich' in response or 'meine' in response:
                stoppuhr('starte meine stoppuhr')
            else:
                stoppuhr('starte die stoppuhr')
        else:
            luna.say('Okay. Dann mach ich nichts.')
    elif 'stell' in text or 'beginn' in text:
        pass
    else:
        # hier muss noch das ganze verfollständigt werden
        text = 'Timer abgelaufen.'
        if 'essen' in text:
            text = 'Guck doch mal nach deinem Essen.'
        E_eins = {'Zeit': luna.analysis['datetime'], 'Text': text, 'Benutzer': luna.user}
        if 'timer' in luna.local_storage.keys():
            luna.local_storage['timer'].append(E_eins)
        else:
            luna.local_storage['timer'] = [E_eins]


def stopwatch(text, luna):
    if 'start' in text:
        if 'mein' in text:
            nutzer = luna.user
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'stoppuhr' in nd.keys():
                luna.say('Es läuft bereits eine Stoppuhr. Soll ich diese erst stoppen?')
                response = luna.listen()
                if 'ja' in text:
                    luna.say('Alles klar. Die alte Stoppuhr wurde bei {} gestoppt und eine neue gestartet.')
                    nd['stoppuhr'] = datetime.datetime.now()
            else:
                luna.say('Alles klar, Stoppuhr wurde um {} gestartet'.format(get_time(datetime.datetime.now())))
                nd['stoppuhr'] = datetime.datetime.now()
        else:
            if 'stoppuhr' in luna.local_storage.keys():
                luna.say('Es läuft bereits eine Stoppuhr. Soll ich diese erst stoppen?')
                response = luna.listen()
                if 'ja' in text:
                    luna.say('Alles klar. Die alte Stoppuhr wurde bei {} gestoppt und eine neue gestartet.')
                    luna.local_storage['stoppuhr'] = datetime.datetime.now()
            else:
                luna.say('Alles klar, die Stoppuhr wurde um {} gestartet.'.format(get_time(datetime.datetime.now())))
                luna.local_storage['stoppuhr'] = datetime.datetime.now()

    elif 'stopp' in text or 'beende' in text:
        if 'mein' in text:
            nutzer = luna.nutzer
            nutzerdictionary = luna.local_storage.get('users')
            nd = nutzerdictionary.get(nutzer)
            if 'stoppuhr' in nd.keys():
                luna.say('Alles klar, die Stoppuhr wurde um {} gestoppt. Sie dauerte {}.'.format(
                    get_time(nd['stoppuhr']), get_time_differenz(nd['stoppuhr'])))
            else:
                luna.say('Es wurde noch keine Stoppuhr gestartet. Soll ich eine starten?')
                response = luna.listen()
                if 'ja' in response:
                    luna.say(
                        'Alles klar, Stoppuhr wurde um {} gestartet'.format(
                            get_time(get_time(datetime.datetime.now()))))
                    nd['stoppuhr'] = datetime.datetime.now()
        else:
            if 'stoppuhr' in luna.local_storage.keys():
                luna.say('Alles klar, die Stoppuhr wurde um {} gestoppt. Sie dauerte {}.'.format(
                    get_time(datetime.datetime.now()), get_time_differenz(luna.local_storage['stoppuhr'], datetime.datetime.now(), luna)))
                luna.local_storage['stoppuhr'] == []
            else:
                luna.say('Es wurde noch keine Stoppuhr gestartet. Soll ich eine starten?')
                response = luna.listen()
                if 'ja' in response:
                    luna.say('Alles klar, Stoppuhr wurde um {} gestartet'.format(
                        get_time(get_time(datetime.datetime.now()))))
                    luna.local_storage['stoppuhr'] = datetime.datetime.now()

    else:
        luna.say(
            'Ich kann die Stoppuhr nur starten oder stoppen.')  # bald sollte noch eine Pause-Funktion hinzugefügt werden


def countdown(text, luna):
    text = text.split(' ')
    timecode = -1
    for i in range(len(text)):
        if text[i] is 'von':
            timecode = int(text[i + 1])
    if 'minute' in text:
        timecode = timecode * 60
    elif 'stunde' in text:
        luna.say('Ist das nicht ein bisschen zu lang?')
        response = luna.listen()
        if 'nein' in text:
            timecode = timecode * 3600

    if timecode is not -1:
        for i in range(timecode):
            time = timecode - i
            luna.say(str(time))
            sleep(1)
    else:
        luna.say('Tut mir leid, leider habe ich nicht verstanden, von wo ich herunter zählen soll')

def get_time_differenz(start_time, time, luna):
    aussage = []
    dz = time - start_time
    print(dz)
    years = datetime.strptime(dz, '%Y')
    months = datetime.strptime(dz, '%m')
    days = datetime.strptime(dz, '%d')
    hours = dz.strptime('%H')
    minutes = datetime.strptime(dz, '%M')
    seconds = datetime.strptime(dz, '%S')

    if years is 1:
        aussage.append('einem Jahr')
    elif years > 1:
        aussage.append(str(years) + ' Jahren')
    if months is 1:
        aussage.append('einem Monat')
    elif months > 1:
        aussage.append(str(months) + ' Monaten')
    if days is 1:
        aussage.append('einem Tag')
    elif days > 1:
        aussage.append(str(days) + ' Tagen')
    if hours is 1:
        aussage.append('einer Stunde')
    elif hours > 1:
        aussage.append(str(hours) + ' Stunden')
    if minutes is 1:
        aussage.append('einer Minute')
    elif minutes > 1:
        aussage.append(str(minutes) + ' Minuten')
    if seconds is 1:
        aussage.append('einer Sekunde')
    elif seconds > 1:
        aussage.append(str(seconds) + ' Sekunden')

    return luna.enumerate(aussage)


def get_time(i):
    stunde = i.hour
    nächste_stunde = stunde + 1
    if nächste_stunde == 24:
        nächste_stunde = 0
    minute = i.minute
    stunde = str(stunde)
    minute = str(minute)
    if minute == 0:
        ausgabe = stunde + ' Uhr.'
    elif minute == 5:
        ausgabe = 'fünf nach ' + stunde
    elif minute == 10:
        ausgabe = 'zehn nach ' + stunde
    elif minute == 15:
        ausgabe = 'viertel nach ' + stunde
    elif minute == 20:
        ausgabe = 'zwanzig nach ' + stunde
    elif minute == 25:
        ausgabe = 'fünf vor halb ' + stunde
    elif minute == 30:
        ausgabe = 'halb ' + nächste_stunde
    elif minute == 35:
        ausgabe = 'fünf nach halb ' + nächste_stunde
    elif minute == 40:
        ausgabe = 'zwanzig vor ' + nächste_stunde
    elif minute == 45:
        ausgabe = 'viertel vor ' + nächste_stunde
    elif minute == 50:
        ausgabe = 'zehn vor ' + nächste_stunde
    elif minute == 55:
        ausgabe = 'fünf vor ' + nächste_stunde
    else:
        ausgabe = stunde + ' Uhr ' + minute
    return ausgabe


def get_day(i):
    now = datetime.datetime.now()
    wochentag = datetime.datetime.today().weekday()
    tage = {0: 'Montag', 1: 'Dienstag', 2: 'Mittwoch', 3: 'Donnerstag', 4: 'Freitag', 5: 'Samstag', 6: 'Sonntag'}
    nummern = {1: 'erste', 2: 'zweite', 3: 'dritte', 4: 'vierte', 5: 'fünfte',
               6: 'sechste', 7: 'siebte', 8: 'achte', 9: 'neunte', 10: 'zehnte',
               11: 'elfte', 12: 'zwölfte', 13: 'dreizehnte', 14: 'vierzehnte', 15: 'fünfzehnte',
               16: 'sechzehnte', 17: 'siebzehnte', 18: 'achtzehnte', 19: 'neunzehnte', 20: 'zwanzigste',
               21: 'einundzwanzigste', 22: 'zweiundzwanzigste', 23: 'dreiundzwanzigste', 24: 'vierundzwanzigste',
               25: 'fünfundzwanzigste', 26: 'sechsundzwanzigste', 27: 'siebenundzwanzigste', 28: 'achtundzwanzigste',
               29: 'neunundzwanzigste', 30: 'dreißigste', 31: 'einunddreißigste', 32: 'zweiunddreißigste'}
    ausgabe = 'Heute ist ' + tage.get(wochentag) + ' der ' + nummern.get(now.day) + ' ' + nummern.get(now.month) + '.'
    return ausgabe


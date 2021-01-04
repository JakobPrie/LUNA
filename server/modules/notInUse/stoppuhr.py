# Beschreibung
'''
--- Timer ---
Dieses Modul ermöglicht es einen Timer zu starten
'''

import datetime

def isValid(text):
    text = text.lower()
    if ('starte' in text or 'starten' in text or 'beginne' in text  or 'fang' in text) and 'stoppuhr' in text:
        return True
    elif ('stoppe' in text or 'beende' in text) and 'stoppuhr' in text:
        return True
    elif 'stelle' in text and 'auf' in text:
        return True


def handle(text, luna, profile):
    text = text.lower()
    now = datetime.datetime.now()
    timedelta = datetime.timedelta()
    if ('starte' in text or 'starten' in text or'beginne' in text  or 'fang' in text) and 'stoppuhr' in text:
        luna.say('Teimer gestartet um ' + get_time(now))
        luna.local_storage['stoppuhr'] = datetime.datetime.now()
    if 'stoppe' in text or 'stopp' in text or 'beende' in text:
        if 'stoppuhr' in luna.local_storage.keys():
            start = luna.local_storage.get('stoppuhr')
            end = datetime.datetime.now()
            delta = end - start
            print(delta)
            luna.say('Teimer um ' + get_time(datetime.datetime.now()) + ' gestoppt. ')
            luna.say('Teimer lief seit ' + get_time_delta(delta))
        else:
            luna.say('Es wurde noch kein Teimer gestartet.')


def get_time(time):
     now = time
     stunde = time.hour
     nächste_stunde = time.hour + 1
     if nächste_stunde == 24:
        nächste_stunde = 0
     minute = time.minute
     stunde = str(stunde)
     minute = str(minute)
     print('Methode: get_Time')
     print('Werte festgelegt........')
    
     if minute == 0:
        ausgabe = stunde + ' Uhr'
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

def get_time_delta(delta):
    print('Methode: get_time_delta')
    yearInt = delta.year
    monthInt = delta.month
    weeksInt = delta.week
    dayInt = delta.day
    hourInt = delta.hours
    minuteInt = delta.minute
    secondsInt = delta.second
    print('Integer-Werte festgelegt..........')

    aussage = ''

    if yearInt == 1:
        aussage += 'einem Jahr, '
    elif yearInt > 1:
        aussage += year + ' Jahren, '
    elif monthInt == 1:
        aussage+= 'einem Monat, '
    elif monthInt > 1:
        aussage += month + ' Monate, '
    if dayInt == 1:
        aussage += 'ein Tag, '
    elif dayInt > 1:
        aussage += day + ' Tage, '
    elif hourInt == 1:
        aussage += 'einer Stunde,'
    elif hourInt > 1:
        aussage += hour + ' Stunden,'
    elif minuteInt == 1:
        aussage += ' einer Minute,'
    elif minuteInt > 1:
        aussage += ' ' + minute + ' Minuten,'

    elif secondsInt == 1:
        aussage += ' einer Sekunde.'
    elif secondsInt > 1:
        aussage += ' ' + seconds + ' Sekunden.'
    
    return aussage

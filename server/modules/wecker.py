import datetime
from phue import Bridge

SECURE = True


def isValid(text):
    text = text.lower()
    if 'weck ' in text or 'wecke' in text:
        return True

def handle(text, luna, profile):
    text = text.lower()
    time = luna.analysis["time"]
    minute = str(time['minute']) if time['minute'] != 0 else ''
    """
    if not 'morgens' in text and not 'früh' in text and not 'abends' in text:
        luna.say("Meintest du {} Uhr {} morgens oder Abends?".format(str(time['hour']-12), minute))
        response =luna.listen()
        if 'morgens' in text or 'früh' in text:
            time = time -12
    """
    stunde = str(time['hour'])
    if 'lösch' in text or 'beend' in text:
        if 'täglich' in text or 'jeden tag' in text:
            days = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]
            try:
                time = luna.analysis["time"]
                wecker = {'Zeit': time, 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Täglichen Wecker um {} Uhr {} gelöcht.".format(stunde, minute))
            except:
                luna.say("Welchen Wecker soll ich ausschalten?")
                for item in luna.local_storage["regular_alarm"].keys():
                    print(item)
                    if item['Benutzer'] == luna.user:
                        stunde = item["Zeit"]["hour"]
                        minute = item["Zeit"]["minute"]
                        luna.say("{} Uhr {}".format(stunde, minute))
                response = luna.listen()
                wecker = {'Zeit': luna.Analyzer.analyze(response)['time'], 'Benutzer': luna.user}
                for item in luna.local_storage["regular_alarm"].keys():
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Täglichen Wecker um {} Uhr {} gelöscht.". format(wecker['Zeit']['hour'], wecker['Zeit']['minute']))

        elif 'wochenende' in text:
            days = ["samstag", "sonntag"]
            try:
                time = luna.analysis["time"]
                wecker = {'Zeit': time, 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Täglichen Wecker um {} Uhr {} gelöcht.".format(stunde, minute))
            except:
                luna.say("Welchen Wecker soll ich ausschalten?")
                for item in days:
                    if item['Benutzer'] == luna.user:
                        stunde = item["Zeit"]["hour"]
                        minute = item["Zeit"]["minute"]
                        luna.say("{} Uhr {}".format(stunde, minute))
                response = luna.listen()
                wecker = {'Zeit': luna.Analyzer.analyze(response)['time'], 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Wecker am Wochenende um {} Uhr {} gelöscht.". format(wecker['Zeit']['hour'], wecker['Zeit']['minute']))

        elif 'wochentag' in text or 'unter der woche' in text:
            days = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag"]
            try:
                time = luna.analysis["time"]
                wecker = {'Zeit': time, 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Täglichen Wecker um {} Uhr {} gelöcht.".format(stunde, minute))
            except:
                luna.say("Welchen Wecker soll ich ausschalten?")
                for item in days:
                    if item['Benutzer'] == luna.user:
                        stunde = item["Zeit"]["hour"]
                        minute = item["Zeit"]["minute"]
                        luna.say("{} Uhr {}".format(stunde, minute))
                response = luna.listen()
                wecker = {'Zeit': luna.Analyzer.analyze(response)['time'], 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Wecker unter der Woche um {} Uhr {} gelöscht.".format(wecker['Zeit']['hour'], wecker['Zeit']['minute']))

        elif 'jeden' in text or 'jedem' in text:
            days = get_text_beetween('jeden', text)
            for item in days:
                if item.lower() not in ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]:
                    days.remove(item)
            try:
                time = luna.analysis["time"]
                wecker = {'Zeit': time, 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Täglichen Wecker um {} Uhr {} gelöcht.".format(stunde, minute))
            except:
                luna.say("Welchen Wecker soll ich ausschalten?")
                for item in days:
                    if item['Benutzer'] == luna.user:
                        stunde = item["Zeit"]["hour"]
                        minute = item["Zeit"]["minute"]
                        luna.say("{} Uhr {}".format(stunde, minute))
                response = luna.listen()
                wecker = {'Zeit': luna.Analyzer.analyze(response)['time'], 'Benutzer': luna.user}
                for item in days:
                    luna.local_storage["regular_alarm"][item].remove(wecker)
                luna.say("Wecker unter der Woche um {} Uhr {} gelöscht.".format(wecker['Zeit']['hour'], wecker['Zeit']['minute']))

        else:
            if 'Wecker' in luna.local_storage.keys():
                wecker = {'Zeit': luna.analysis['datetime'], 'Benutzer': luna.user}
                luna.local_storage['Wecker'].remove(wecker)
                luna.say("Wecker gelöscht: {}, {} Uhr {}".format(get_reply(luna, time), stunde, minute))
            else:
                luna.say("Für diesem Tag hast du noch keinen Wecker gestellt.")

    else:
        if 'täglich' in text or 'jeden tag' in text or 'jeden morgen' in text or 'jeden abend' in text:
            wecker = {'Zeit': time, 'Benutzer': luna.user}
            for item in luna.local_storage["regular_alarm"].keys():
                luna.local_storage["regular_alarm"][item].append(wecker)
            luna.say("Wecker gestellt für jeden Tag um {} Uhr {}.".format(stunde, minute))
        elif 'wochenende' in text:
            wecker = {'Zeit': time, 'Benutzer': luna.user}
            luna.local_storage["regular_alarm"]["samstag"].append(wecker)
            luna.local_storage["regular_alarm"]["sonntag"].append(wecker)
            luna.say("Wecker gestellt für jeden Samstag und Sonntag um {} Uhr {}". format(stunde, minute))
        elif 'wochentags' in text or 'unter der woche' in text:
            wecker = {'Zeit': time, 'Benutzer': luna.user}
            luna.local_storage["regular_alarm"]["montag"].append(wecker)
            luna.local_storage["regular_alarm"]["dienstag"].append(wecker)
            luna.local_storage["regular_alarm"]["mittwoch"].append(wecker)
            luna.local_storage["regular_alarm"]["donnerstag"].append(wecker)
            luna.local_storage["regular_alarm"]["freitag"].append(wecker)
            luna.say("Wecker gestellt für jeden Wochentag um {} Uhr {}.". format(stunde, minute))
        elif 'jeden' in text or 'jedem' in text:
            wecker = {'Zeit': time, 'Benutzer': luna.user}
            days = get_text_beetween('jeden', text)
            for item in days:
                if item.lower() in ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]:
                    luna.local_storage["regular_alarm"][item.lower()].append(wecker)
                else:
                    days.remove(item)
            luna.say("Wecker gestellt für jeden {} um {} Uhr {}.".format(get_enumerate(days), stunde, minute))
        else:
            wecker = {'Zeit': luna.analysis['datetime'], 'Benutzer': luna.user}
            if 'Wecker' in luna.local_storage.keys():
                luna.local_storage['Wecker'].append(wecker)
            else:
                luna.local_storage['Wecker'] = [wecker]
            print(time)
            luna.say("Wecker gestellt für {}, {} Uhr {}".format(get_reply(luna, time), stunde, minute))

def get_reply(luna, time):
    now = datetime.datetime.today().day
    monat = str(time['month'])
    tag = str(time['day'])
    if int(monat) <= 9:
        monat = '0' + monat
    if len(tag) == 1:
        tag = '0' + tag
    tage = {'01': 'ersten', '02': 'zweiten', '03': 'dritten', '04': 'vierten', '05': 'fünften',
            '06': 'sechsten', '07': 'siebten', '08': 'achten', '09': 'neunten', '10': 'zehnten',
            '11': 'elften', '12': 'zwölften', '13': 'dreizehnten', '14': 'vierzehnten', '15': 'fünfzehnten',
            '16': 'sechzehnten', '17': 'siebzehnten', '18': 'achtzehnten', '19': 'neunzehnten', '20': 'zwanzigsten',
            '21': 'einundzwanzigsten', '22': 'zweiundzwanzigsten', '23': 'dreiundzwanzigsten',
            '24': 'vierundzwanzigsten',
            '25': 'fünfundzwanzigsten', '26': 'sechsundzwanzigsten', '27': 'siebenundzwanzigsten',
            '28': 'achtundzwanzigsten',
            '29': 'neunundzwanzigsten', '30': 'dreißigsten', '31': 'einunddreißigsten', '32': 'zweiunddreißigsten'}
    monate = {'01': 'Januar', '02': 'Februar', '03': 'März', '04': 'April', '05': 'Mai', '06': 'Juni',
              '07': 'Juli', '08': 'August', '09': 'September', '10': 'Oktober', '11': 'November',
              '12': 'Dezember'}
    print(tag, now)
    if int(tag) == int(now):
        return 'heute'
    elif tag == now+1:
        return 'morgen'
    elif tag == now+2:
        return 'übermorgen'
    else:
        luna_output = tage.get(tag) + monate.get(monat)
        telegram_output = tag + '.' + monat
        return 'den ' + luna.correct_output(luna_output, telegram_output)

def get_text_beetween(start_word, text, end_word='', output='array'):
    ausgabe = []
    index = -1
    text = text.split(' ')
    for i in range(len(text)):
        if text[i] is start_word:
            index = i + 1
    if index is not -1:
        if end_word is '':
            while index <= len(text):
                ausgabe.append(text[index])
                index += 1
        else:
            founded = False
            while index <= len(text) and not founded:
                if text[index] is end_word:
                    founded = True
                else:
                    ausgabe.append(text[index])
                    index += 1
    if output is 'array':
        return ausgabe
    elif output is 'String':
        ausgabe_neu = ''
        for item in ausgabe:
            ausgabe += item + ' '
        return ausgabe

def get_enumerate(array):
    new_array = []
    for item in array:
        new_array.append(item.strip(' '))
    ausgabe = ''
    if len(new_array) == 0:
        pass
    elif len(new_array) == 1:
        ausgabe = array[0]
    else:
        for item in range(len(new_array) - 1):
            ausgabe += new_array[item] + ', '
        ausgabe = ausgabe.rsplit(', ', 1)[0]
        ausgabe = ausgabe + ' und ' + new_array[-1]
    return ausgabe

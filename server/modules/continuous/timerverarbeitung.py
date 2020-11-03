import datetime

INTERVALL = 2

def run(luna, profile):
    now = datetime.datetime.now()
    if 'Timer' in luna.local_storage.keys():
        timer = luna.local_storage.get('Timer')
        for item in timer:
            benutzer = item['Benutzer']
            output = item['Text']
            zeit = item['Zeit']
            ausgabe = output
            differenz = zeit - now
            dic = {'Text': ausgabe, 'Benutzer': benutzer}
            if differenz.total_seconds() <= 0:
                luna.start_module(user=benutzer, name='timerausgabe', text=dic)
                timer.remove(item)
                luna.local_storage['Timer'] = erinnerungen

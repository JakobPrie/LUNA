import datetime

INTERVALL = 2

def run(luna, profile):
    now = datetime.datetime.now()
    if 'timer' in luna.local_storage.keys():
        timer = luna.local_storage.get('timer')
        for item in timer:
            benutzer = item['Benutzer']
            output = item['Text']
            zeit = item['Zeit']
            '''zeit = datetime.datetime.strptime(zeit, '%Y-%m-%d %H:%M:%S.%f')'''
            ausgabe = output
            #print(now)
            #print(zeit)
            differenz = zeit - now
            dic = {'Text': ausgabe, 'Benutzer': benutzer}
            if differenz.total_seconds() <= 0:
                luna.start_module(user=benutzer, name='timerausgabe', text=dic)
                timer.remove(item)
                luna.local_storage['timer'] = erinnerungen

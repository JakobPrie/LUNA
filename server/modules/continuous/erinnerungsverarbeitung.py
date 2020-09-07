import datetime

INTERVALL = 2

def run(luna, profile):
    now = datetime.datetime.now()
    if 'Erinnerungen' in luna.local_storage.keys():
        erinnerungen = luna.local_storage.get('Erinnerungen')
        for item in erinnerungen:
            benutzer = item['Benutzer']
            output = item['Text']
            zeit = item['Zeit']
            '''zeit = datetime.datetime.strptime(zeit, '%Y-%m-%d %H:%M:%S.%f')'''
            if 'dass ' in output:
                ausgabe = 'Ich sollte dir Bescheid sagen, ' + output + '.'
            else:
                ausgabe = 'Ich sollte dich ans ' + output + ' erinnern'
            #print(now)
            #print(zeit)
            differenz = zeit - now
            dic = {'Text': ausgabe, 'Benutzer': benutzer}
            if differenz.total_seconds() <= 0:
                luna.start_module(user=benutzer, name='erinnerungsausgabe', text=dic)
                erinnerungen.remove(item)
                luna.local_storage['Erinnerungen'] = erinnerungen

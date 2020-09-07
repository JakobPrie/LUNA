import datetime

INTERVALL = 2

def run(luna, profile):
    now = datetime.datetime.now()
    if 'Wecker' in luna.local_storage.keys():
        erinnerungen = luna.local_storage.get('Wecker')
        for item in erinnerungen:
            benutzer = item['Benutzer']
            zeit = item['Zeit']
            '''zeit = datetime.datetime.strptime(zeit, '%Y-%m-%d %H:%M:%S.%f')'''
            differenz = zeit - now
            if differenz.total_seconds() <= 0:
                ausgabe = 'Guten Morgen {}. Ich hoffe, du hast gut geschlafen'.format(benutzer)
                try:
                    geburtsdatum = luna.local_storage['users'][luna.user]['date_of_birth']
                    month = int(geburtsdatum['month'])
                    day = int(geburtsdatum['day'])
                    now = datetime.datetime.now()
                    if now.month == month and now.day == day:
                        ausgabe = 'Herzlichen Glückwunsch zum Geburtstag {}. Ich hoffe, du hast einen großartigen Tag.'.format(
                            benutzer)
                except KeyError:
                    '''Do nothing'''

                dic = {'Benutzer': benutzer, 'Text': ausgabe}
                ton = "morgen_ihr_luschen.wav"
                luna.start_module(user=benutzer, name='wecker_audio_ausgabe', text=ton)
                luna.start_module(user=benutzer, name='weckerausgabe', text=dic)
                erinnerungen.remove(item)
                luna.local_storage['Wecker'] = erinnerungen

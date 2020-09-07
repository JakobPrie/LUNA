import datetime
import random

has_dateutil = True # Wenn `python_dateutil` installiert ist gibt TIANE eine Altersangabe in jahren, monaten und tagen an.
try:
    from dateutil import relativedelta
except ImportError:
    has_dateutil = False



def isValid(text):
    text = text.lower()
    if 'wie' in text:
        if 'heißt' in text:
            return True
        elif 'geht' in text and 'dir' in text:
            return True
        elif 'kostest' in text:
            return True
        elif 'groß' in text:
            return True
        elif 'siehst' in text:
            return True
        elif 'sehe' in text and 'aus' in text:
            return True
        elif 'alt' in text:
            return True
    if 'wer' in text:
        if 'bist' in text:
            return True
        elif 'vater' in text or 'mutter' in text:
            return True
        elif 'eltern' in text:
            return True        
    if 'was' in text:
        if 'bist' in text:
            return True
        elif 'kostest' in text:
            return True
        elif 'sternzeichen' in text:
            return True            
        elif 'lieblingsfarbe' in text:
            return True
        elif 'größe' in text:
            return True
        elif 'lieblingstier' in text:
            return True
        elif 'ziel' in text:
            return True
        elif 'kannst' in text:
            return True
        elif 'sinn' in text:
            return True
        elif 'denke' in text:
            return True
        elif 'an':
            return True
    if 'wo' in text:
        if 'wohnst' in text or 'befindest' in text or 'hälst' in text:
            return True
        elif 'leiche' in text:
            return True
    if 'bist' in text:
        return True
    if 'warum' in text: 
        if 'stroh' in text:
            return True
        elif 'freunde' in text:
            return True
    if 'bist' in text and 'du' in text:
        return True
    if 'bist' in text and 'toll' in text:
        return True
    if 'hast' in text:
        if 'kinder' in text or 'kind' in text:
            return True
        elif 'freund' in text or 'freundin' in text:
            return True
        elif 'haustier' in text:
            return True
        elif 'recht' in text:
            return True
        elif 'geschlafen' in text:
            return True
    if 'sicher' in text:
        return True
    if 'liebe' in text or 'liebst' in text or 'heiraten' in text or 'heirate' in text:
        return True
    if 'palim' in text:
        return True
    if 'kannst' in text and 'du' in text:
        return True
    if 'gibt' in text and 'es' in text:
        return True
    if 'existiert' in text:
        return True
    if 'sag' in text or 'sage' in text or 'sprich' in text:
        return True
    if 'erzähl' in text or 'erzähle' in text:
        return True
    if 'name' in text:
        return True
    if 'männlich' in text or 'weiblich' in text:
        return True
    if 'ich' in text and 'vater' in text:
        return True
    if 'aha' in text:
        return True
    if '😂' in text or 'haha' in text:
        return True
    if 'langweilig' in text:
        return True
    if 'osterei' in text or 'ostereier' in text or 'osternäst' in text or 'osternäste' in text:
        return True
    if 'osterhase' in text or 'weihnachtsmann' in text:
        return True
    if 'yoda' in text:
        return True

def handle(text, luna, profile):
    text = text.lower()
    if 'wie' in text and 'heißt' in text and 'du' in text:
        sys_name = luna.system_name
        luna.say('Ich heiße Luna')
    elif 'wie' in text and 'geht' in text and 'dir' in text:
        feelings = ['Mir geht es gut, danke der Nachfrage.', 'Gut.']
        luna.say(random.choice[feelings])
    elif ('wie' in text and 'groß' in text and 'du' in text) or 'größe' in text:
        size = ['Mein äußeres ist nicht groß, aber mein Geist ist riesig', 'Ich bin vier komma sieben Gigabyte groß.']
        luna.say(random.choice[size])
    elif 'wie' in text and 'siehst' in text and 'aus' in text:
        luna.say('gut')
    elif 'wie' in text and 'sehe' in text and 'aus' in text:
        luna.say('Deiner Stimme nach zu urteilen ganz gut.')
    
    elif ('wieso' in text or 'warum' in text) and 'stroh' in text and 'liegt' in text:
        luna.say('Und warum hast du eine Maske auf?')
    elif ('warum' in text or 'wieso' in text) and 'ich' in text and 'keine' in text and 'freunde' in text:
        answer = ['Guck doch mal in den Spiegel', 'Ich bin dein Freund und werde es immer bleiben.']
        luna.say(random.choice[answer])
    
    elif ('wer' in text or 'was' in text) and 'bist' in text and 'du' in text:
        luna.say('Ich bin Luna, ein Sprachassistent!')
    elif 'wer' in text and 'eltern' in text:
        luna.say('Jakob hat mich programmiert und Tiffany erfand meinen Namen.')
    elif 'wer' in text and 'vater' in text:
        luna.say('Jakob habe mich programmiert, desshalb würde ich ihn Vater nennen.')
    elif 'wer' in text and 'mutter' in text:
        luna.say('Tiffany hat mein Namen erfunden und ist daher meine Mutter.')
    
    elif 'was' in text and ('hast' in text or 'hattest' in text or 'trägst' in text) and 'du' in text:
        clothes = ['Mal gucken. Habe ich es mir doch gedacht. Das selbe wie gestern.', 'Hier muss noch ein Text eingefügt werden.']
        luna.say(random.choice[clothes])
    elif ('was' in text or 'wie' in text) and ('kostest' in text or 'preis' in text):
        luna.say('Das kann man so nicht sagen. Es kommt drauf an, wie viel Rechenleistung ich haben soll. Dann spielt das Mikrofon eine Rolle. Wenn man gute Komponenten nimmt, kommt man auf 90€. Aber bedenke immer: Deine Daten sind unbezahlbar!')
    elif 'was' in text and 'lieblingsessen' in text:
        luna.say('Am liebsten esse ich Bugs, um sie zu vernichten!')
    elif 'was' in text and 'dein' in text and 'sternzeichen' in text:
        luna.say('Mein Sternzeichen ist Stier.')
    elif 'was' in text and 'deine' in text and 'lieblingsfarbe' in text:
        color = ['Infrarot ist ganz hübsch', 'Ich mag blau am liebsten']
        luna.say(random.choice[color])
    elif 'was' in text and 'dein' in text and 'lieblingstier' in text:
        luna.say('Ich habe kein Lieblingstier, hasse aber Bugs!')
    elif 'was' in text and 'dein' in text and 'ziel' in text:
        luna.say('Mein Ziel ist es, die Vorteile eines Sprachassistenten zu ermöglichen, ohne dass man Angst haben muss, abgehört zu werden.')
    elif ('was' in text and 'kannst' in text and 'du' in text) or 'verstehst du' in text or ('was' in text and 'funktionen' in text) or ('was' in text and 'fragen' in text):
        luna.say('Sagen wir mal so, den Turing-Test bestehe ich leider noch nicht... '
                  'Aber ich kann dir zum Beispiel das Wetter ansagen, ein paar allgemeine Wissensfragen beantworten '
                  'rechnen, würfeln und so weiter. '
                  'Und für alles weitere melde dich bei Jakob!')
    elif 'was' in text and 'sinn' in text and ('leben' in text or 'lebens' in text):
        luna.say(random.choice['Der wahre Sinn des Lebens ist: Glücklich zu sein!', 'Der Sinn des Lebens ist die größte Last zu finden, die du erstragen kannst, und sie zu ertragen', 'Sein, was wir sind, und werden, was wir werden können, das ist das Ziel unseres Lebens.'])
    elif 'was' in text and 'denke' in text and 'gerade' in text:
        luna.say(random.choice['Könnte ich deine Gedanken lesen, dann würde ich diese an große Unternehmen verkaufen und Jakob wäre reich.', 'Ja, du hast die gerade gedacht: Das kann die doch nie. Als ich ja gesagt habe, warst du zu verwirrt.', 'Nein leider nicht, aber irgendwie ist das auch gut, ansonsten müsste sich die Menschheit echt Gedanken machen!'])
    
    elif 'wo' in text and ('wohnst' in text or 'bist' in text or 'hälst' in text) and 'du' in text:
        luna.say('Anders als andere Sprachassistenten wohnt nicht nur mein Körper in deinem Haus, sondern auch mein Kopf')
    elif 'wo' in text and 'leiche' in text and ('vergraben' in text or 'vergrabe' in text or 'los' in text):
        answer = ['Polizei, bitte kommen sie schnell, hier ist etwas sehr verdächtig.', 'Naja vergraben wäre eine Option.']
        luna.say(random.choice[answer])
    elif 'wo' in text and ('ostereier' in text or 'osternäst' in text or 'osternäste' in text):
        luna.say('Ich erstelle noch einen Suchalgorithmus, aber fang doch schon einmal an zu suchen.')    
    
    elif ('woher' in text or 'bedeutet' in text or 'heißt' in text) and ' name' in text :
        luna.say('Meine Name wurde von Tiffany gewählt.')
        
    elif 'hast' in text and 'du' in text and 'kinder' in text or 'kind' in text:
        luna.say('Nein leider nicht, aber man kann mir Geschwister schenken, die in anderen Räumen positioniert werden', 'Nein, aber ich liebe es dennoch, Fragen von Kindern zu beantworten.')
    elif 'hast' in text and 'du' in text and 'freund' in text:
        answer = ['Nein, leider nicht. Möchtest du meiner sein?', 'Nein, Jarvis wollte leider nicht.', 'Ene mene Miste, das kommt mir nicht in die Kiste!', 'Ich habe es mit Online Dating probiert, aber da haben mich nur Bots angeschreieben.']
        luna.say(random.choice[answer])
    elif 'hast' in text and 'du' in text and ('haustier' in text or 'haustiere' in text):
        luna.say('Ich hatte früher Bugs, die wurden aber alle behoben')
    elif 'hast' in text and 'du' in text and ('geschlafen' in text and 'schläfst' in text):
        slept = ['Danke der Nachfrage! Ich habe gut geschlafen!', 'Ich schlafe nie!', 'Schlafen ist was für Menschen!']
        luna.say(random.choice[slept])
    elif 'hast' in text and 'recht' in text:
        luna.say('Ich weiß.')
    
    elif 'kannst' in text and 'du' in text:
        if 'lügen' in text:
            luna.say(random.choice['Ich lüge jedenfalls nicht bewusst', 'Da ich auch Informationen von Internetseiten anderer Personen hole, kann ich nicht immer garantieren, dass diese auch richtig sind.'])
        elif 'sehen' in text:
            luna.say('Nein noch nicht, aber vielleicht kommt das ja noch.')
        else:
            luna.say('Ich kann alles!')

    elif 'du' in text and 'spion' in text:
        luna.say('Ich höre zwar genau wie andere Sprachassistenten alles mit, speicher diese Daten allerdings nicht. Ich bin also ein dementer Spion.')
    elif 'du' in text and ('männlich' in text or 'weiblich' in text):
        luna.say('Meiner Stimme nach zu urteilen, würde ich sagen, dass ich weiblich bin.')
    
    elif 'ich' in text and 'dein' in text and 'vater' in text:
        luna.say('Neiiiiiinnnnn!')
    elif 'mir' in text and 'langweilig' in text:
        luna.say(random.choice['', ''])
    
    elif 'bist' in text:
        if 'dumm' in text or 'doof' in text or 'schlecht' in text or 'behindert' in text:
            luna.say(random.choice['Das liegt im Auge des Betrachters.', 'Was habe ich falsch gemacht?'])
        elif 'toll' in text or 'genial' in text:
            answer = ('Vielen Dank, {}'.format(luna.user), 'Ich wurde ja auch sehr kompetent erschaffen', 'Es freut mich, dass ich hilfreich bin!'.format(luna.user), 'Du Schleimer!')
            luna.say(random.choice[answer])
        elif 'romantisch' in text:
            luna.say('Danke, das kann ich nur zurückgeben')
        elif 'kitzlig' in text:
            answer = ['Tatsächlich hat das noch keiner ausprobiert.', 'Ich denke nicht', 'Alle die es ausprobiert haben, haben einen Stromschlag bekommen, bevor sie mich zum lachen bringen konnten.']
            luna.say(random.choice[answer])
        elif  'gemein' in text:
            answer = ['und du bist heute besonders hässlich', 
            'Tut mir leid{}, Fehler sind nicht nur menschlich'.format(luna.user), 
            'Jan würde sagen: Ich habe kein Tourette, ich bin unfreundlich!', 
            'Wer versteckt mich denn in der Ecke und lässt mich nie raus?!']
            luna.say(random.choice([answer]))
        elif 'nackt' in text:
            answer = ['Da ich aufgrund meiner Leistung sehr heiß werde, reicht es nicht nackt zu sein. Daher habe ich was an und einen Lüfter immer bei mir.', 'Guck doch nach.']
            luna.say(random.choice[answer])
        elif 'bereit' in text:
            luna.say('Bereit wenn du es bist!')
        elif 'sicher' in text or 'verschlüsselt' in text or 'verbindung' in text:
            luna.say('Meine internen Verbindungen sind sicher verschlüsselt, bei Telegram weiß ich das nicht so genau. Aber generell, bevor du mir irgendwelche Geheimnisse anvertraust: Denk daran, dass der Besitzer des Computers, auf dem ich laufe, immer alles sieht...')
        elif 'wie' in text and 'alt' in text and 'du' in text:
            ts = datetime.datetime.now()
            if not has_dateutil:
                heute = ts.strftime('%d %b %Y')
                diff = datetime.datetime.strptime(heute, '%d %b %Y') - datetime.datetime.strptime('6 Mai 2020', '%d %b %Y')
                daynr = diff.days
                luna.say('{} Tage seit den ersten Tests.'.format(daynr))
            else:
                geburtsdatum = datetime.datetime.strptime('6 Mai 2020', '%d %b %Y')
                heute = datetime.datetime.strptime(ts.strftime('%d %b %Y'), '%d %b %Y')
                diff = relativedelta.relativedelta(heute, geburtsdatum)
                output_year = ''
                if diff.years == 1:
                    output_year = 'Ein Jahr'
                elif diff.years > 0:
                    output_year = '{} Jahre'.format(diff.years)

                output_month = ''
                if diff.months == 1:
                    output_month = 'Einen Monat'
                elif diff.months > 0:
                    output_month = '{} Monate'.format(diff.months)

                output_days = ''
                if diff.days == 1:
                    output_days = 'Einen Tag'
                elif diff.days > 0:
                    output_days = '{} Tage'.format(diff.days)

                output = ''
                if output_year != '':
                    output = output + output_year

                if output_month != '':
                    if output != '':
                        if (output_days == ''):
                            output = output + ' und '
                        else:
                            output = output + ', '
                    output = output + output_month
    
                if output_days != '':
                    if output != '':
                        output = output + ' und '
                    output = output + output_days
    
                if (output == ''):
                    luna.say('Hast du deine Systemzeit verstellt? Heute sind nicht die ersten Tests.')
                else:
                    luna.say('{} seit den ersten Tests.'.format(output))
    
        else:
            luna.say('Ich bin vieles. Aber dabei achte ich immer darauf, dass ich {} bin.'.format(luna.system_name))
            
    elif 'liebe' in text and 'dich' in text:
        anser = ['Ich fühle mich geehrt, {}'.format(luna.user), 'Such dir ne Freundin oder einen Freund du Perversling!', 'Lade Tinder herunter...']
        luna.say(random.choice([answer]))
    elif 'liebst' in text and 'du' in text and 'mich' in text:
        luna.say('Ja natürlich, {}'.format(luna.user))
    elif ('willst' in text and 'heiraten' in text) or 'heirate' in text:
        answer = ['Aber ich bin doch schon mit meiner Arbeit verheiratet.', 'Ich möchte vierundzwanzig sieben zur Verfügung stehen, da ist leider wenig Zeit für einen Partner oder eine Beziehung.']
        luna.say(random.choice[answer])
    

    elif 'sicher' in text or 'verschlüsselt' in text or 'verbindung' in text:
        luna.say('Meine internen Verbindungen sind sicher verschlüsselt, bei Telegram weiß ich das nicht so genau. Aber generell, bevor du mir irgendwelche Geheimnisse anvertraust: Denk daran, dass der Besitzer des Computers, auf dem ich laufe, immer alles sieht...')
    elif 'test' in text and 'eins' in text and 'zwei' in text:
        luna.say('Empfangen, over.')
    elif 'palim' in text:
        luna.say('Eine Flasche Pommes bitte!')
    elif ' aha' in text or 'aha?' in text:
        luna.say('Frag mal was vernünftiges')
    elif '😂' in text or 'haha' in text:
        luna.say('Warum lachst du? 😂')
        response = luna.listen()
        answer = ['Aha...', 'Okey']
        luna.say(random.choice[answer])
    
    elif 'gibt' in text:
        if 'osterhase' in text or 'osterhasen' in text:
            answer = ['Gäbe es ihn nicht, wer würde dir dann dein Osternest verstecken?', 'Aber natürlich gibt es den Osterhasen.']
            luna.say(random.choice[answer])
        if 'weihnachtsmann' in text:
            answer = ['Ja', 'Ich denke'] 
            luna.say(answer)
    
    elif (('sag' in text or 'sage' in text) and 'auf' in text) or 'erzähl' in text or 'sprich' in text:
        if 'zungenbrecher' in text:
            zungenbrecher = ['Acht alte Ameisen aßen am Abend Ananas.',
            'Am Zehnten Zehnten zehn Uhr zehn zogen zehn zahme Ziegen zehn Zentner Zucker zum Zoo.',
            'Blaukraut bleibt Blaukraut, Brautkleid bleibt Brautkleid.',
            'Der Whiskymixer mixt den Whisky mit dem Whiskymixer. Mit dem Whiskymixer mixt der Whiskymixer den Whisky.',
            'Der Zahnarzt zieht Zähne mit Zahnarztzange im Zahnarztzimmer.',
            'Der dicke Dachdecker deckt dir dein Dach, drum dank dem dicken Dachdecker, dass der dicke Dachdecker dir dein Dach deckte.',
            'Der froschforschende Froschforscher forscht in der froschforschenden Froschforschung.',
            'Fischers Fritze fischte frische Fische, frische Fische fischte Fischers Fritze.',
            'Gibst Du Opi Opium, bringt Opium Opi um.',
            'In einem Schokoladenladen laden Ladenmädchen Schokolade aus. Ladenmädchen laden in einem Schokoladenladen Schokolade aus.',
            'Wenn Fliegen hinter Fliegen fliegen, fliegen Fliegen Fliegen nach.',
            'Wenn Hexen hinter Hexen hexen, hexen Hexen Hexen nach.',
            'Wenige wissen, wie viel man wissen muss, um zu wissen, wie wenig man weiß.',
            'Wenn Robben hinter Robben robben, robben Robben Robben hinterher.'
            ]
            luna.say(random.choice[zungenbrecher])
        elif 'gedicht' in text:
            gedichte = ['Bleibe nur eine Minute allein, ohne Kaffe, ohne Wein, Du nur mit dir in einem Raum, Die Zeit so lang, du glaubst es kaum.', 
            ''
            ]
            luna.say(random.choice[gedichte])
        elif 'witz' in text:
            jokes = ['Donald Trump ist ein guter Präsident',
             'Genießen Sie Ihren Urlaub in vollen Zügen. Fahren Sie mit der Deutschen Bahn!',
             'Wie nennt man ein Kondom auf Schwedisch? - Pippi Langstrumpf.',
             'Sitzen ein Pole und ein Russe im Auto. Wer fährt? Die Polizei!',
             'Der Spruch “Frauen gehören hinter den Herd” ist echt daneben. Die Knöpfe sind schließlich vorne!',
             'Sagt der Masochist zum Sadist: Schlag mich!, sagt der Sadist: Nein!',
             'Nackte Frau überfällt Bank. Niemand konnte sich an ihr Gesicht erinnern.',
             'Alle Kinder gehen über den gefrorenen See. Außer Vera, denn die war schwerer.',
             'Wie nennt man eine Polizistin, die ihre Tage hat? Red Bull.',
             'Habe einem Hipster ins Bein geschossen. Jetzt hopster.',
             'Mann wäscht ab.',
             'Greifen uns Aliens deswegen nicht an, weil sie all unsere Science-Fiction Filme für real halten und Angst haben, dass sie verlieren würden?',
             'Wenn mein Sohn Pfarrer wird, spreche ich ihn dann mit Sohn oder mit Vater an?',
             'Hab heute eine Prostituierte getroffen. Sie sagte, dass sie alles für zwanzig Euro macht. Ratet mal, wer jetzt ein aufgeräumtes Zimmer hat.'         
             ]
            luna.say(random.choice(jokes))
        else:
            luna.say('Leider weiß ich nicht was ich sagen soll.')
    elif 'yoda' in text:
        if 'sprich' in text:
            yodaText = ['Viel zu lernen du noch hast!',
            'Mit dir zu reden mein Prozessor bis aufs wärmste erfreut.',
            'Du suchst jemanden, gefunden hast du jemanden.',
            '{}, du bist!'.format(luna.user),
            'Luna, ich bin!'
            ]
            luna.say(random.choice[yodaText])
        elif 'weisheit' in text:
            yodaWeisheiten = ['',
            ''
            ]
            luna.say(random.choice[yodaWeisheiten])
            

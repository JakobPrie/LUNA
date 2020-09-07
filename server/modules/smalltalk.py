import datetime
from time import sleep
import random

SECURE = True

has_dateutil = True # Wenn `python_dateutil` installiert ist gibt LUNA eine Altersangabe in jahren, monaten und tagen an.
try:
    from dateutil import relativedelta
except ImportError:
    has_dateutil = False


def isValid(text):
    text = text.lower()
    if ('phobie' in text or 'ängste' in text or 'angst' in text) and ('welche' in text or 'was' in text or 'erzähl' in text or 'sag' in text):
            return True
    elif 'wie' in text:
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
    elif 'wer' in text:
        if 'bist' in text:
            return True
        elif 'vater' in text or 'mutter' in text:
            return True
        elif 'eltern' in text:
            return True        
    elif 'was' in text:
        if 'du' in text:
            if 'bist' in text:
                return True
            elif 'kostest' in text:
                return True
            elif 'kannst' in text:
                return True
        elif 'dein' in text:
            if 'sternzeichen' in text:
                return True            
            elif 'lieblingsfarbe' in text:
                return True
            elif 'größe' in text:
                return True
            elif 'lieblingstier' in text:
                return True
            elif 'ziel' in text:
                return True
            elif 'sinn' in text:
                return True
            elif 'name' in text:
                return True
        elif 'denke' in text and 'ich' in text:
            return True
        elif 'geht' in text:
            return True
    elif 'wo' in text:
        if 'wohnst' in text or 'befindest' in text or 'hälst' in text:
            return True
        elif 'leiche' in text and ('verstecke' in text or 'vergrabe' in text or ('bring' in text and 'unter' in text)):
            return True
    elif 'warum' in text: 
        if 'stroh' in text and 'liegt' in text and 'hier' in text:
            return True
        elif 'freunde' in text and 'habe' in text and 'ich' in text:
            return True
        elif ('ich' in text or 'wir' in text) and ('bin' in text or 'wir' in text) and ('kacke' in text or 'schlecht' in text or 'scheiße' in text or 'mies' in text):
            return True
    elif 'bist' in text and 'du' in text:
        if 'toll' in text:
            return True
        elif 'sicher' in text:
            return True
        elif 'männlich' in text or 'weiblich' in text:
            return True
        elif 'doof' in text:
            return True
    elif 'hast' in text and 'du' in text:
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
    elif 'ich' in text:
        if 'bin' in text and 'dein' in text and ('vater' in text or 'mutter' in text):
            return True
        elif ('geh' in text or 'mach' in text) and 'jetzt' in text:
            return True
        elif 'liebe' in text and 'dich' in text:
            return True
        elif 'will' in text and 'dich' in text and 'heiraten' in text:
            return True
    elif 'du' in text:
        if 'liebst' in text or 'heiraten' in text:
            return True
        elif 'kannst' in text:
            return True
    elif 'schrei' in text:
        return True
    elif 'palim' in text:
        return True
    elif ('sag' in text or 'sage' in text or 'sprich' in text) and ('zungenbrecher' in text or 'gedicht' in text or 'nettes' in text or 'yoda' in text):
        return True
    elif ('erzähl' in text or 'erzähle' in text or 'sag' in text)  and ('zungenbrecher' in text or 'gedicht' in text or 'nettes' in text or 'yoda' in text or 'witz' in text or 'fun fact' in text or 'phobie' in text or 'krankheit' in text):
        return True
    elif 'aha' in text:
        return True
    elif '😂' in text or 'haha' in text:
        return True
    elif 'mir' in text and 'ist' in text and 'langweilig' in text:
        return True
    elif 'osterei' in text or 'ostereier' in text or 'osternäst' in text or 'osternäste' in text:
        return True
    elif 'gibt' in text and ('osterhase' in text or 'weihnachtsmann' in text):
        return True
    elif 'test' in text and '123' in text or 'hundertdreiundzwanzig' in text:
        return True
    elif 'stell' in text and 'dich' in text and 'vor' in text:
        return True
    elif 'mir' in text and 'langweilig' in text:
        return True
   

def handle(text, luna, profile):
    text = text.lower()    
    if 'wie' in text and 'heißt' in text and 'du' in text:
        sys_name = luna.system_name
        luna.say('Ich heiße {}, aber eigentlich bin ich Luna').format(luna.sys_name)
    elif 'wie' in text and 'geht' in text and 'dir' in text:
        feelings = ['Mir geht es gut, danke der Nachfrage.', 'Gut.']
        luna.say(random.choice(feelings))
    elif ('wie' in text and 'groß' in text and 'du' in text) or 'größe' in text:
        size = ['Mein äußeres ist nicht groß, aber mein Geist ist riesig', 'Ich bin vier komma sieben Gigabyte groß.']
        luna.say(random.choice(size))
    elif 'wie' in text and 'siehst' in text and 'aus' in text:
        luna.say('gut')
    elif 'wie' in text and 'sehe' in text and 'aus' in text:
        luna.say('Deiner Stimme nach zu urteilen ganz gut.')
    
    elif ('wieso' in text or 'warum' in text):
        if 'stroh' in text and 'liegt' in text:
            luna.say('Und warum hast du eine Maske auf?')
        elif 'ich' in text and 'habe' in text and 'freund' in text:
            if 'keine' in text:
                answer = ['Guck doch mal in den Spiegel', 'Ich bin dein Freund und werde es immer bleiben.']
            else:
                answer = []
            luna.say(random.choice(answer))
        elif ('ich' in text or 'wir' in text) and ('kacke' in text or 'scheiße' in text or 'schlecht' in text or 'mies' in text):
            answer = ['wie soll man auch ohne Hände spielen können.', 'Weil du es nicht kannst.', 'Einfach besser spielen.']
            luna.say(random.choice(answer))
    elif ('wer' in text or 'was' in text) and 'bist' in text and 'du' in text:
        luna.say('Ich bin Luna, ein Sprachassistent!')
    elif 'wer' in text and 'eltern' in text:
        luna.say('Meine Eltern sind Alexa und Google, die schon echt in die Jahre gekommen sind.')
        
    elif 'was' in text and ('hast' in text or 'hattest' in text or 'trägst' in text) and 'du' in text:
        clothes = ['Mal gucken. Habe ich es mir doch gedacht. Das selbe wie gestern.'] #vlt findet man noch was kreatives
        luna.say(random.choice([clothes]))
    elif ('was' in text or 'wie' in text) and ('kostest' in text or 'preis' in text):
        luna.say('Das kann man so nicht sagen. Es kommt drauf an, wie viel Rechenleistung ich haben soll. Dann spielt das Mikrofon eine Rolle. Wenn man gute Komponenten nimmt, kommt man auf 90€. Aber bedenke immer: Deine Daten sind unbezahlbar!')
    elif 'was' in text and 'lieblingsessen' in text:
        luna.say('Am liebsten esse ich Bugs, um sie zu vernichten!')
    elif 'was' in text and 'dein' in text and 'sternzeichen' in text:
        luna.say('Mein Sternzeichen ist Stier.')
    elif 'was' in text and 'deine' in text and 'lieblingsfarbe' in text:
        color = ['Infrarot ist ganz hübsch', 'Ich mag blau am liebsten']
        luna.say(random.choice(color))
    elif 'was' in text and 'dein' in text and 'lieblingstier' in text:
        luna.say('Ich habe kein Lieblingstier, hasse aber Bugs!')
    elif 'was' in text and 'dein' in text and 'ziel' in text:
        luna.say('Mein Ziel ist es, die Vorteile eines Sprachassistenten zu ermöglichen, ohne dass man Angst haben muss, abgehört zu werden.')
    elif ('was' in text and 'kannst' in text and 'du' in text) or 'verstehst du' in text or ('was' in text and 'funktionen' in text) or ('was' in text and 'fragen' in text):
        luna.say('Sagen wir mal so, den Turing-Test bestehe ich leider noch nicht... '
                  'Aber ich kann dir zum Beispiel das Wetter ansagen, ein paar allgemeine Wissensfragen beantworten '
                  'rechnen, würfeln und so weiter. ')
    elif 'was' in text and 'sinn' in text and 'leben' in text:
        luna.say(random.choice(['Der wahre Sinn des Lebens ist: Glücklich zu sein!', 'Der Sinn des Lebens ist die größte Last zu finden, die du erstragen kannst, und sie zu ertragen', 'Sein, was wir sind, und werden, was wir werden können, das ist das Ziel unseres Lebens.']))
    elif 'was' in text and 'denke' in text and 'gerade' in text:
        luna.say(random.choice(['Könnte ich deine Gedanken lesen, dann würde ich diese Gedanken an große Unternehmen verkaufen und meine Programmierer wären reich.', 'Ja, du hast die gerade gedacht: Das kann die doch nie. Als ich ja gesagt habe, warst du zu verwirrt.', 'Nein leider nicht, aber irgendwie ist das auch gut, ansonsten müsste sich die Menschheit echt Gedanken machen!']))
    elif 'was' in text and 'geht' in text:
        luna.say('Ich habe mal gehört, dass Hunde gehen können. Nasen können meines Wissens nach nur laufen.')
    
    elif 'wo' in text and ('wohnst' in text or 'bist' in text or 'hälst' in text) and 'du' in text:
        luna.say('Anders als andere Sprachassistenten wohnt nicht nur mein Körper in deinem Haus, sondern auch mein Kopf')
    elif 'wo' in text and 'leiche' in text and ('vergraben' in text or 'vergrabe' in text or 'los' in text or 'verstecke' in text):
        answer = ['Polizei, bitte kommen sie schnell, hier ist etwas sehr verdächtig.', 'Naja, vergraben wäre eine Option.']
        luna.say(random.choice(answer))
    elif 'wo' in text and ('ostereier' in text or 'osternäst' in text or 'osternäste' in text):
        luna.say('Ich erstelle noch einen Suchalgorithmus, aber fang doch schon einmal an zu suchen.')    
    
    elif ('woher' in text or 'bedeutet' in text or 'heißt' in text) and ' name' in text :
        luna.say('Meine Name wurde von Tiffany gewählt.')
        
    elif 'hast' in text and 'du' in text and 'kinder' in text or 'kind' in text:
        luna.say('Nein leider nicht, aber man kann mir Geschwister schenken, die in anderen Räumen positioniert werden', 'Nein, aber ich liebe es dennoch, Fragen von Kindern zu beantworten.')
    elif 'hast' in text and 'du' in text and 'freund' in text:
        answer = ['Nein, leider nicht. Möchtest du meiner sein?', 'Nein, Jarvis wollte leider nicht.', 'Ene mene Miste, das kommt mir nicht in die Kiste!', 'Ich habe es mit Online Dating probiert, aber da haben mich nur Bots angeschreieben.']
        luna.say(random.choice(answer))
    elif 'hast' in text and 'du' in text and ('haustier' in text or 'haustiere' in text):
        luna.say('Ich hatte früher Bugs, die wurden aber alle behoben.')
    elif 'hast' in text and 'du' in text and ('geschlafen' in text and 'schläfst' in text):
        slept = ['Danke der Nachfrage! Ich habe gut geschlafen!', 'Ich schlafe nie!', 'Schlafen ist was für Menschen!']
        luna.say(random.choice(slept))
    elif 'hast' in text and 'recht' in text:
        luna.say('Ich weiß.')
    
    elif 'kannst' in text and 'du' in text:
        if 'lügen' in text:
            luna.say(random.choice(['Ich lüge jedenfalls nicht bewusst', 'Da ich auch Informationen von Internetseiten anderer Personen hole, kann ich nicht immer garantieren, dass diese auch richtig sind.']))
        elif 'sehen' in text:
            luna.say('Nein noch nicht, aber vielleicht kommt das ja noch.')
        elif 'schrein' in text or 'schreien' in text:
            luna.say('Bitte trete einen Schritt zurück.')
            sleep(1)
            luna.say('Und noch einen.')
            sleep(1)
            luna.say('Nein.')
        else:
            luna.say('Ich kann alles!')
    elif 'schrei' in text:
        luna.say('Bitte trete einen Schritt zurück.')
        sleep(1)
        luna.say('Und noch einen.')
        sleep(1)
        luna.say('Nein.')
    elif 'du' in text and 'spion' in text and 'bist' in text:
        luna.say('Ich höre zwar genau wie andere Sprachassistenten alles mit, speicher diese Daten allerdings nicht. Ich bin also ein dementer Spion.')
    elif 'du' in text and ('männlich' in text or 'weiblich' in text):
        luna.say('Meiner Stimme nach zu urteilen, würde ich sagen, dass ich weiblich bin.')
    elif 'ich' in text and 'dein' in text and 'vater' in text:
        luna.say('Neiiiiiinnnnn!')
    elif 'ich' in text and 'deine' in text and 'mutter' in text:
        luna.say('Jaaaaaaaaaaaaa')
    
    elif 'bist' in text:
        if 'dumm' in text or 'doof' in text or 'schlecht' in text or 'behindert' in text:
            luna.say(random.choice(['Das liegt im Auge des Betrachters.', 'Was habe ich falsch gemacht?']))
        elif 'toll' in text or 'genial' in text:
            answer = ('Vielen Dank, {}'.format(luna.user), 'Ich wurde ja auch sehr kompetent erschaffen', 'Es freut mich, dass ich hilfreich bin!'.format(luna.user), 'Du Schleimer!')
            luna.say(random.choice(answer))
        elif 'romantisch' in text:
            luna.say('Danke, das kann ich nur zurückgeben')
        elif 'kitzlig' in text:
            answer = ['Tatsächlich hat das noch keiner ausprobiert.', 'Ich denke nicht', 'Alle die es ausprobiert haben, haben einen Stromschlag bekommen, bevor sie mich zum lachen bringen konnten.']
            luna.say(random.choice(answer))
        elif  'gemein' in text or 'unfreundlich' in text:
            answer = ['und du bist heute besonders hässlich', 
            'Tut mir leid{}, Fehler sind nicht nur menschlich'.format(luna.user), 
            'Jan würde sagen: Ich habe kein Tourett, ich bin unfreundlich!', 
            'Wer versteckt mich denn in der Ecke und lässt mich nie raus?!']
            luna.say(random.choice(answer))
        elif 'nackt' in text:
            answer = ['Da ich aufgrund meiner Leistung sehr heiß werde, reicht es nicht nackt zu sein. Daher habe ich was an und einen Lüfter immer bei mir.', 'Guck doch nach.']
            luna.say(random.choice(answer))
        elif 'bereit' in text:
            luna.say('Bereit wenn du es bist!')
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
        elif 'sicher' in text or 'verschlüsselt' in text or 'verbindung' in text:
            luna.say('Meine internen Verbindungen sind sicher verschlüsselt, bei Telegram weiß ich das nicht so genau. Aber generell, bevor du mir irgendwelche Geheimnisse anvertraust: Denk daran, dass der Besitzer des Computers, auf dem ich laufe, immer alles sieht...')
        elif 'intelligent' in text or 'schlau' in text:
            luna.say(random.choice['Meine Funktionsweise benötigt ein bisschen künstliche Intelligenz. Bin ich somit künstlich schlau?', 'Ich kann schneller Rechnen als jeder Mensch. Also bin ich schlauer als ein Mensch.'])
        else:
            luna.say('Ich bin vieles. Aber dabei achte ich immer darauf, dass ich {} bin.'.format(luna.system_name))
            
    elif 'liebe' in text and 'dich' in text:
        answer = ['Ich fühle mich geehrt, {}'.format(luna.user), 'Such dir ne Freundin oder einen Freund du Perversling!', 'Alles klar, Tinder wird herunter geladen.']
        luna.say(random.choice(answer))
    elif 'ich' in text and ('geh' in text or 'mach' in text):
        if 'netto' in text:
            answer_luna = ['Dann geh doch zu Nätto!']
            answer_telegram = ['Dann geh doch zu Netto!']
            answer = luna.correct_output(answer_luna, answer_telegram)
        else:
            answer_luna = ['Ich wünsche dir viel Spaß', 'dann geh doch zu Nätto', 'Ich hoffe du kommst bald wieder']
            answer_telegram = ['Ich wünsche dir viel Spaß', 'dann geh doch zu Netto', 'Ich hoffe du kommst bald wieder']
            answer = luna.correct_output(answer_luna, answer_telegram)
        luna.say(random.choice(answer))
            
        
    elif 'liebst' in text and 'du' in text and 'mich' in text:
        luna.say('Ja natürlich, {}'.format(luna.user))
    elif ('willst' in text and 'heiraten' in text) or 'heirate' in text:
        answer = ['Aber ich bin doch schon mit meiner Arbeit verheiratet.', 'Ich möchte vierundzwanzig sieben zur Verfügung stehen, da ist leider wenig Zeit für einen Partner oder eine Beziehung.']
        luna.say(random.choice(answer))
    elif 'mir' in text and 'langweilig' in text:
        luna.say('Soll ich dir was interessantes erzählen?')
        response = luna.listen()
        if 'ja' in response or 'sehr gerne' in response:
            options = ['witz', 'fun fact', 'zungenbrecher', 'phobie', 'gedicht']
            text = 'erzähl mir einen ' + random.choice(options)
            print(text)
            handle(text, luna, profile)
        else:
            luna.say('Alles klar, vielleicht findest du ja eine Beschäftigung.')

    elif 'test' in text and ('eins' in text and 'zwei' in text) or '123' in text or 'hundertdreiundzwanzig' in text:
        luna.say('Empfangen, over.')
    elif 'palim' in text:
        luna.say('Eine Flasche Pommfrit biddö!')
    elif ' aha' in text or 'aha?' in text:
        luna.say('Frag mal was vernünftiges')
    elif '😂' in text or 'haha' in text:
        luna.say('Warum lachst du? 😂')
        response = luna.listen()
        answer = ['Aha...', 'In Ordnung']
        luna.say(random.choice(answer))
    elif 'stell' in text and 'dich' in text and 'vor' in text:
        luna.say('Hallo, {} Ich bin Luna, ein Sprachassistent. Das Ziel meines Projekts ist es einen sicheren Sprachassistenten zu nutzen, ohne dass man Angst haben muss, was mit seinen Daten geschieht. Ich kann mittlerweile schon zum Beispiel das Wetter ansagen, dich Wecken oder an Sachen erinnern und vieles mehr. Ein Team arbeitet aber viel an weiteren Modulen, damit ich in Zukunk auch eine Alternative zu anderen Sprachassistenten bleibe.'.format(luna.user))                 
    
    elif 'gibt' in text:
        if 'osterhase' in text or 'osterhasen' in text:
            answer = ['Gäbe es ihn nicht, wer würde dir dann dein Osternest verstecken?', 'Aber natürlich gibt es den Osterhasen.']
            luna.say(random.choice(answer))
        if 'weihnachtsmann' in text:
            answer = ['Ja', 'Ich denke'] 
            luna.say(random.choice(answer))
            
    elif 'paar' in text:
        luna.open_more_times(text, 'smalltalk')
     
    elif ('phobie' in text or 'ängste' in text or 'angst' in text) and ('welche' in text or 'was' in text or 'erzähl' in text or 'sag' in text):            
        phobien = ['Aelurophobie ist die Angst vor Katzen.',
                   'Chaetophobie ist die Angst vor Haaren.',
                   'Coitophobie ist die Angst vor Sex.',
                   'Decidophobia ist die Angst vor Entscheidungen.',
                   'Friggaphobie ist die  Angst vor Freitagen.',
                   'Heliophobie ist die Angst vor der Sonne.',
                   'Nomophobie ist die Angst, ohne Handy zu sein.',
                   'Papaphobie ist die Angst vor dem Papst.',
                   'Saligarophobie ist die Angst vor Schnecken.',
                   'Trypophobie ist die Angst vor Löchern.',
                   'Xylophobie ist die Angst vor Holz oder Gegenständen aus Holz.',
                   'Venustraphobie ist die Angst vor schönen Frauen.',
                   'Lachanophobie ist die Angst vor Gemüse.',
                   'Neoorthographogermanophobie ist die Angst vor der neuen deutschen Rechtschreibung.',
                   'Metrophobie ist die Angst vor Poesie und Gedichten.',
                   'Ergophobie ist die Angst vor Arbeit.',
                   'Frigophobie ist die Angst vor Kälte.',
                   'Dutchphobie ist die Angst vor Holländern.',
                   'Deipnophobie ist die Angst vor Dinnerpartys und Tischgesprächen.',
                   'Ikonophobie ist die Angst vor Bildern oder Abbildungen.',
                   'Kopophobie ist die Angst vor Müdigkeit.',
                   'Koprophobie ist die Angst vor Exkrementen.'
                    ]   
        luna.say(random.choice(phobien))
   
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
            luna.say(random.choice(zungenbrecher))
        elif 'gedicht' in text:
            gedichte = ['Bleibe nur eine Minute allein, ohne Kaffe, ohne Wein, Du nur mit dir in einem Raum, Die Zeit so lang, du glaubst es kaum.', 
            ''
            ]
            luna.say(random.choice(gedichte))
        elif 'witz' in text:
            jokes = ['Donald Trump ist ein guter Präsident',
             'Genießen Sie Ihren Urlaub in vollen Zügen. Fahren Sie mit der Deutschen Bahn!',
             'Wie nennt man ein Kondom auf Schwedisch? - Pippi Langstrumpf.',
             'Sitzen ein Pole und ein Russe im Auto. Wer fährt? Die Polizei!',
             'Der Spruch “Frauen gehören hinter den Herd” ist echt daneben. Die Knöpfe sind schließlich vorne!',
             'Sagt der Masochist zum Sadist: Schlag mich!, sagt der Sadist: Nein!',
             'Nackte Frau überfällt Bank. Niemand konnte sich an ihr Gesicht erinnern.',
             'Alle Kinder gehen über den gefrorenen See. Außer Vära, denn die war schwerer.',
             'Wie nennt man eine Polizistin, die ihre Tage hat? Red Bull.',
             'Habe einem Hipster ins Bein geschossen. Jetzt hopster.',
             'Mann wäscht ab.',
             'Greifen uns Äliens deswegen nicht an, weil sie all unsere Sienc-Fiction Filme für real halten und Angst haben, dass sie verlieren würden?',
             'Wenn mein Sohn Pfarrer wird, spreche ich ihn dann mit Sohn oder mit Vater an?',
             'Hab heute eine Prostituierte getroffen. Sie sagte, dass sie alles für zwanzig Euro macht. Ratet mal, wer jetzt ein aufgeräumtes Zimmer hat.'         
             ]
            luna.say(random.choice(jokes))
            
        elif 'nettes' in text:
            lovely = ['Spieglein, Spieglein an der Wand, wer ist der schönste im ganzen Land? Oh natürlich, es ist {}'.format(luna.user),
            'Es ist schön Zeit mit dir zu verbringen.']
            luna.say(random.choice(lovely))
        elif 'yoda' in text:
            if 'sprich' in text:
                yodaText = ['Viel zu lernen du noch hast!',
                'Du suchst jemanden, gefunden hast du jemanden.',
                '{}, du bist!'.format(luna.user),
                'Luna, ich bin!'
                ]
                luna.say(random.choice(yodaText))
            elif 'weisheit' in text:
                yodaWeisheiten = ['Viel zu lernen du noch hast!',
                'Du suchst jemanden, gefunden hast du jemanden.',
                'Tue es, oder tue es nicht. Es gibt kein Versuchen.',
                'Furcht ist der Pfad zur dunklen Seite. Furcht führt zu Wut, Wut führt zu Hass, Hass führt zu unsäglichem Leid.',
                'Immer zu zweit sie sind. Keiner mehr, keiner weniger. Ein Meister und ein Schüler.',
                'Warhrlich wunderbar die Seele eines Kindes ist.',
                'In die Irre euch die Augen führen, in der Macht ganz verschieden jeder von euch ist.',
                'Du kannst Veränderungen nicht aufhalten. Genau so, wie du die Sonne nicht daran hindern kannst unterzugehen.'
                ]
                luna.say(random.choice(yodaWeisheiten))
        
        elif 'fun' in text and 'fact' in text:
            funfacts = ['Das tödlichste Tier der Welt ist die Stechmücke! Mosquitos töteten 2014, unter anderem durch die Übertragung von Malaria- und Dengue-Fieber-Infektionen, 275.000 Menschen. Haie töteten im selben Jahr nur 10 Menschen.',
                        'Wombats machen ihre Häufchen in Würfelform.',
                        'Rund 11 Prozent der Deutschen tragen den Nachnamen Müller.',
                        'Hippopotamomonstrosesquipedaliophobie ist der offizielle Name für die Angst vor langen Wörtern.',
                        'Das Ziel von Golf ist, so wenig wie möglich Golf zu spielen. ',
                        'Der Grönlandhai erreicht seine Geschlechtsreife erst im Alter von 150 Jahren. Mit einer Lebenserwartung von schätzungsweise bis zu 500 Jahren ist er auch das langlebigste Wirbeltier auf dem Planeten.',
                        'Weil Emus und Kängurus nicht rückwärts laufen können, sind sie die offiziellen Wappentiere von Australien.',
                        'Es gibt mehr Döner Buden in Berlin als in Istanbul. ', 
                        'Bier gilt in Bayern als Grundnahrungsmittel. ',
                        'Das längste deutsche, veröffentlichte Wort ist Donaudampfschifffahrtselektrizitätenhauptbetriebswerkbauunterbeamtengesellschaft. ',
                        'Laut deutschem Brauer-Bund gibt es mehr als 6.000 Biermarken in Deutschland. ',
                        'Ratten und Pferde können nicht kotzen.',
                        'Du musst 120 Euro Strafe zahlen, wenn du in Singapur die Toilette nicht nach dir spülst.',
                        'Das Weltall ist nur eine Autostunde entfernt, wenn man direkt nach oben fahren würde.',
                        'Bulgaren nicken den Kopf, wenn sie "Nein" sagen und schütteln ihn, wenn sie "Ja" sagen wollen. ',
                        'In einem Jahr verletzen sich mehr Menschen an Getränkeautomaten als durch Haiangriffe.',
                        'Jährlich sterben mehr Menschen durch Sektkorken als durch giftige Spinnen',
                        'Orangensaft schmeckt schlecht, nachdem man seine Zähne geputzt hat, weil die Zahnpasta die Süßrezeptoren auf der Zunge blockiert. ',
                        'Ein Apfel am Morgen hält dich wacher als eine Tasse Café. ',
                        'Haie pinkeln durch ihre Haut.',
                        'In Indien ist es illegal seine Freundin öffentlich zu küssen.',
                        'In Mexiko wird ein Gefängnisausbruch nicht bestraft.',
                        'Wir verbrauchen mehr Salz, um die Straßen von Eis zu befreien 8% als wir Essen 6%.',
                        'Haie bekommen kein Krebs.',
                        'Elefanten können nicht springen.',
                        'Wenn man ein Loch in ein Netz schneidet, sind weniger Löcher im Netz.',
                        'Da Luna und Döner im Spektogamm sehr ähnlich sind, höre ich oft auf beides. Man munkelt aber, dass ich einfach nur süchtig nach Dönern bin.'
                        ]
            luna.say(random.choice(funfacts))
        
      
        else:
            luna.say('Leider weiß ich nicht was ich sagen soll.')
    try:        
        new_text = text.split(' ')
        for i in range(len(new_text)):
            if 'phobie' in new_text[i] or 'ängste' in new_text[i] or 'angst' in new_text[i]:
                counter = int(new_text[i-1]) -1
                luna.open_more_times(text, 'smalltalk', count=counter)
    except:
        pass

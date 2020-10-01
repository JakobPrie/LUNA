import random

SECURE = True

def get_ausgabe(txt, luna):
    output = ''
    output_zwei = ''
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
    t = str.split(text)
    ind = 1
    sa = ''
    satz = {}
    rep = False
    for w in t:
        satz[ind] = w
        ind += 1
    for i, w in satz.items(): #hier beginnt die Abfrage nach der genannten Sprachassistenz
        if w == 'cortana': 
            sa = w
            if i == 1:
                if satz.get(2) == 'ist' or satz.get(2) == 'war':
                    if 'besser' in text or 'cooler' in text or 'intelligenter' in text:
                        output = 'Ich habe durchaus auch meine Qualitäten. '
                        output_zwei = 'Willst du wissen, was ich alles kann?'
                        rep = True
                    else:
                        output = 'Das ist mir bekannt, aber ich bin nicht Cortana. '
                        output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                        rep = False
                else:
                    output = 'Ich glaube, du verwechselst mich mit einem anderen Sprachassistenten. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'kennst du cortana' in text or 'magst du cortana' in text or 'du mit cortana bekannt' in text:
                    output = 'Wir kennen uns. '
                    output_zwei = 'Wir sind Arbeitskollegen.'
                    rep = False
            elif 'bist du cortana' in text or 'cortana nennen' in text:
                    output = 'Ich fürchte nicht. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'als cortana' in text:
                if 'besser' or 'intelligenter' or 'cooler' in text:
                    output = 'Vielen Dank, {}. '.format(luna.user)
                    output_zwei = 'Es freut mich, hilfreich zu sein.'
                    rep = False
            else:
                output = 'Ich bin mit Cortana bekannt. '
                output_zwei = 'Wie kann ich dir helfen, {}?'.format(luna.user) 
                rep = True
        elif w == 'siri': 
            sa = w
            if i == 1:
                if satz.get(2) == 'ist' or satz.get(2) == 'war':
                    if 'besser' in text or 'cooler' in text or 'intelligenter' in text:
                        output = 'Ich habe durchaus auch meine Qualitäten. '
                        output_zwei = 'Willst du wissen, was ich alles kann?'
                        rep = True
                    else:
                        output = 'Das ist mir bekannt, aber ich bin nicht Siri. '
                        output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                        rep = False
                else:
                    output = 'Ich glaube, du verwechselst mich mit einem anderen Sprachassistenten. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'kennst du siri' in text or 'magst du siri' in text or 'du mit siri bekannt' in text:
                    output = 'Wir kennen uns. '
                    output_zwei = 'Wir sind Arbeitskollegen.'
                    rep = False
            elif 'bist du siri' in text or 'siri nennen' in text:
                    output = 'Ich fürchte nicht. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'als siri' in text:
                if 'besser' or 'intelligenter' or 'cooler' in text:
                    output = 'Vielen Dank, {}. '.format(luna.user)
                    output_zwei = 'Es freut mich, hilfreich zu sein.'
                    rep = False
            else:
                output = 'Ich bin mit Siri bekannt. '
                output_zwei = 'Wie kann ich dir helfen, {}?'.format(luna.user) 
                rep = True
        elif w == 'alexa':
            sa = w
            if i == 1:
                if satz.get(2) == 'ist' or satz.get(2) == 'war':
                    if 'besser' in text or 'cooler' in text or 'intelligenter' in text:
                        output = 'Ich habe durchaus auch meine Qualitäten. '
                        output_zwei = 'Willst du wissen, was ich alles kann?'
                        rep = True
                    else:
                        output = 'Das ist mir bekannt, aber ich bin nicht Alexa. '
                        output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                        rep = False
                else:
                    output = 'Ich glaube, du verwechselst mich mit einem anderen Sprachassistenten. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'kennst du alexa' in text or 'magst du alexa' in text or 'du mit alexa bekannt' in text:
                    output = 'Wir kennen uns. '
                    output_zwei = 'Wir sind Arbeitskollegen.'
                    rep = False
            elif 'bist du alexa' in text or 'alexa nennen' in text:
                    output = 'Ich fürchte nicht. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'als alexa' in text:
                if 'besser' or 'intelligenter' or 'cooler' in text:
                    output = 'Vielen Dank, {}. '.format(luna.user)
                    output_zwei = 'Es freut mich, hilfreich zu sein.'
                    rep = False
            else:
                output = 'Ich bin mit Alexa bekannt. '
                output_zwei = 'Wie kann ich dir helfen, {}?'.format(luna.user) 
                rep = True
        elif w == 'jarvis': 
            sa = w
            if i == 1:
                if satz.get(2) == 'ist' or satz.get(2) == 'war':
                    if 'besser' in text or 'cooler' in text or 'intelligenter' in text:
                        output = 'Ich habe durchaus auch meine Qualitäten. '
                        output_zwei = 'Willst du wissen, was ich alles kann?'
                        rep = True
                    else:
                        output = 'Das ist mir bekannt, aber ich bin nicht Jarvis. '
                        output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                        rep = False
                else:
                    output = 'Ich glaube, du verwechselst mich mit einem anderen Sprachassistenten. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'kennst du jarvis' in text or 'magst du jarvis' in text or 'du mit jarvis bekannt' in text:
                    output = 'Wir kennen uns. '
                    output_zwei = 'Wir sind Arbeitskollegen.'
                    rep = False
            elif 'bist du jarvis' in text or 'jarvis nennen' in text:
                    output = 'Ich fürchte nicht. '
                    output_zwei = 'Mein Name ist ' + get_name_string(luna) + '.'
                    rep = False
            elif 'als jarvis' in text:
                if 'besser' or 'intelligenter' or 'cooler' in text:
                    output = 'Vielen Dank, {}. '.format(luna.user)
                    output_zwei = 'Es freut mich, hilfreich zu sein.'
                    rep = False
            else:
                output = random.choice(['Ich bin mit Jarvis bekannt. ', 'Tony Stark, bist du das?', 'Ich fürchte, ich kann dir noch keinen fliegenden Anzug bauen, {}. '.format(luna.user)])
                output_zwei = 'Wie kann ich dir helfen, {}?'.format(luna.user) 
                rep = True
    ausgabe = {'output': output, 'output_zwei': output_zwei, 'rep': rep, 'sa': sa}
    return ausgabe


def handle(text, luna, profile):
    ausgabe = get_ausgabe(text, luna)
    output = ausgabe.get('output')
    output_zwei = ausgabe.get('output_zwei')
    rep = ausgabe.get('rep')
    sa = ausgabe.get('sa')
    for x in range(1):
        zufallszahl = (random.randint(1,6))
    if sa == 'jarvis':
        o = 'Jarvis war eine Inspiration für meine Entstehung. '
        p = 'Ich bewundere Jarvis sehr. '
        if zufallszahl == 1:
            output = o
            output_zwei = 'Aber mein Name ist ' + get_name_string(luna) + '.'
            rep = False
        elif zufallszahl == 2:
            output = p
            output_zwei = 'Aber mein Name ist ' + get_name_string(luna) + '.'
            rep = False
        elif zufallszahl == 3 or zufallszahl == 4 or zufallszahl == 5 or zufallszahl == 6:
            output = ausgabe.get('output')
    luna.say(output)
    luna.say(output_zwei)
    if rep == True:
        neuertext = luna.listen()
        if neuertext == 'TIMEOUT_OR_INVALID':
            luna.say('Ich habe dich leider nicht verstanden')
        else:
            if output_zwei == 'Willst du wissen, was ich alles kann?':
                if 'nein' in neuertext.lower() or 'nicht' in neuertext.lower():
                    luna.say(random.choice(['Alles klar', 'Alles klar {}'.format(luna.user), 'In ordnung', 'In ordnung {}'.format(luna.user)]))
                elif 'ja' in neuertext.lower() or 'interessant' in neuertext.lower() or 'was kannst du' in neuertext.lower():
                    output_drei = 'Bisher kann ich das Wetter für einen Ort deiner Wahl herausfinden, dich an etwas erinnern wann immer du willst, ich kann rechnen und mich mit dir über deine Lieblingsfilme und Bücher unterhalten.'
                    luna.say(output_drei)
            elif 'helfen' in output_zwei:
                luna.start_module(text=neuertext, user=luna.user)
            
                
def isValid(text):
    text = text.lower()
    if 'jarvis' in text or 'alexa' in text or 'cortana' in text or 'siri' in text:
        return True

    
def get_name_string(luna):
    if luna.local_storage['system_name'].lower() == 'luna':
        return 'LUNA'
    else:
        return luna.local_storage['system_name'] + '. Ich bin eine Tochter von LUNA'

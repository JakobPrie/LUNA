import random
import re
from time import sleep

PRIORITY = 3
SECURE = True

zwischenPattern = re.compile(r'.*(von|zwischen) (-?\d+) (und|bis) (-?\d+).*', re.I)
bisPattern = re.compile(r'.*(bis|kleiner gleich) (-?\d+).*', re.I)
kleinerPattern = re.compile(r'.*(unter|kleiner) (als)? (-?\d+).*', re.I)

def output(txt, luna):
    output = ''
    text = tt.lower()
    t = str.split(text)
    if 'münze' in text or ('kopf' in text and 'oder' in text and 'zahl' in text):
        q = random.randint(1,2)
        if q == 1:
            output = 'kopf'
        else:
            output = 'zahl'
    elif 'würfel' in text or 'alea iacta est' in text:
        q = random.randint(1,6)
        if q == 1:
            output = 'eins'
        elif q == 2:
            output = 'zwei'
        elif q == 3:
            output = 'drei'
        elif q == 4:
            output = 'vier'
        elif q == 5:
            output = 'fünf'
        else:
            output = 'sechs'
    elif ('zufall' in text or 'zufällig' in text) and 'zahl' in text:
        match = zwischenPattern.match(text)
        if (output == '' and match is not None):
            if (int(match.group(2)) < int(match.group(4))):
                output = str(random.randint(int(match.group(2)), int(match.group(4))))
            else:
                output = str(random.randint(int(match.group(4)), int(match.group(2))))
        match = bisPattern.match(text)
        if (output == '' and match is not None):
            if (match.group(2) > 0):
                output = str(random.randint(1, int(match.group(2))))
            else:
                output = str(random.randint(int(match.group(2)), 1))
        match = kleinerPattern.match(text)
        if (output == '' and match is not None):
            if (match.group(3) > 0):
                output = str(random.randrange(1, int(match.group(3))))
            else:
                output = str(random.randrange(int(match.group(3)), 1))
                
    elif 'schere' in text or 'stein' in text or 'papier' in text:
        possibilities = ['Schere', 'Stein', 'Papier']
        output = 'Da ist wohl was schief gelaufen'
        zufall = random.randint(0, 2)
        output = possibilities[zufall]
    
    elif 'grade' in text and 'ungerade' in text:
        possibilities = ['grade', 'ungerade']
        output = random.choice(posibilities)
        

    if (output == ''):
        output = str(random.randint(1,100))
    return output

def handle(text, luna, profile):
    ausgabe = output(text, luna).strip()
    if (ausgabe.startswith('-')):
        ausgabe = 'minus ' + ausgabe[1:]
    luna.say('drei')
    sleep(1)
    luna.say('zwei')
    sleep(1)
    luna.say('eins')
    sleep(1)
    luna.say(ausgabe)

def isValid(text):
    text = text.lower()
    if 'münze' in text or ('kopf' in text and 'oder' in text and 'zahl' in text) or 'würfel' in text or (('zufall' in text or 'zufällig' in text) and 'zahl' in text):
        return True
    elif 'schere' in text and 'stein' in text and 'papier' in text:  
        return True
    elif 'grade' in text and 'ungerade' in text:
        return True

class Luna:
   
    def say(self, text):
        print (text)
    def listen(self):
        neuertext = input()
        return neuertext

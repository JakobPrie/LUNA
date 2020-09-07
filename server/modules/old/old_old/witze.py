import random
import datetime

def isValid(text):
    text = text.lower()
    if 'witz' in text and ('kennst' in text or 'erzähl' in text or 'sag' in text or 'sage' in text):
        return True

def handle(text, luna, profile):
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

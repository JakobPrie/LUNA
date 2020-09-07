import random

SECURE = True

def handle(text, luna, profile):
    if luna.user is not None:
        if not luna.user == 'Unknown':
            responses = ['Wenn mich nicht alles täuscht bist du {}',
                         'Ich glaube du bist {}',
                         'Soweit ich das sehen kann bist du {}']
            response = random.choice(responses)
            luna.say(response.format(luna.user))
            return
    responses = ['Das kann ich gerade leider nicht sehen',
                 'Das musst du aktuell leider selbst wissen',
                 'Entschuldige, aber das kann ich leider gerade nicht beurteilen']
    luna.say(random.choice(responses))

def isValid(text):
    text = text.lower()
    if 'wer' in text and 'bin' in text and 'ich' in text:
        return True
    if 'wie' in text and 'heiße' in text and 'ich' in text:
        return True

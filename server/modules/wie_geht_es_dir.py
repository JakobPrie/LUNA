import random

def isValid(text):
    text = text.lower()
    if 'wie' in text and (('geht' in text and 'dir' in text) or 'läuft' in text or 'geht\'s' in text or 'gehts' in text):
        return True
    else:
        return False

def handle(text, luna, profile):
    answers = ['Danke, gut!',
               'Mir gehts gut, {}.'.format(luna.user),
               'Alles gut, {}.'.format(luna.user)]
    luna.say(random.choice(answers))
    luna.say('Und wie geht es dir?')
    reply = luna.listen()
    reply = reply.lower()
    if 'nicht so' in reply or 'schlecht' in reply or 'müde' in reply or 'mies' in reply or 'suboptimal' in reply:
        luna.say('Das ist blöd, aber denk immer daran: Alles hat ein Ende nur die Wurst hat zwei!')
    elif 'gut' in reply or 'besser' in reply or 'bestens' in reply or 'super' in reply or 'wundervoll' in reply or 'glücklich' in reply or 'froh' in reply:
        luna.say('Das freut mich!')
    else:
        luna.say('Ich fürchte, ich konnte dich nicht verstehen. Geht es dir so schlecht?')

PRIORITY = -2
SECURE = True

def isValid(text):
    text = text.lower()
    if 'danke' in text or 'thx' in text or 'thanks' in text:
        return True

def handle(text, luna, local_storage):
    luna.say('[Gerne doch|Keine Ursache], {}.'.format(luna.user))

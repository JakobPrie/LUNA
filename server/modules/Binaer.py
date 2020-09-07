
def isValid(text):
    text = text.lower()
    if 'binär' in text and ('wandle' in text or 'wandel' in text or 'gib' in text):
        return True
    elif ('was' in text or 'wie' in text) and 'binär' in text:
        return True

def handle(text, luna, profile):
    decNumber = getNumber(text)
    if decNumber != 'UNDO':
        luna.say('Die Zahl ' + decNumber + ' ist ' + binary(int(decNumber)) + ' in dem Binären.')
    else:
        luna.say('Ich konnte die Zahl leider nicht herausfiltern.')

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 2, output)
        n = n // 2
    return str(output)

def getNumber(text):
    answer = 'UNDO'
    hotWord = ['wandle', 'wandel', 'gib', 'ist']
    sentence = text.split(' ')
    index = -1
    for item in sentence:
        i = 0
        while i <= len(hotWord):
            if sentence[item] == hotWord[i]:
                index = i + 1
    if index != -1:
        answer = sentence[index]
    return answer

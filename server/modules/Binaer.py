
def isValid(text):
    """
    text = text.lower()
    if 'in' in text and 'binär' in text and ('wandle' in text or 'wandel' in text or 'gib' in text):
        return True
    elif ('was' in text or 'wie' in text) and 'in' in text and 'binär' in text:
        return True
    """
    text = text.lower()
    batch = ["[wandle|wandel|gib] [|in|auf] binär"]
    if batchMatch(batch, text):
        return True
    else:
        return False


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

def batchGen(batch):
    """
    With the batchGen-function you can generate fuzzed compare-strings
    with the help of a easy syntax:
        "Wann [fährt|kommt] [der|die|das] nächst[e,er,es] [Bahn|Zug]"
    is compiled to a list of sentences, each of them combining the words
    in the brackets in all different combinations.
    This list can then fox example be used by the batchMatch-function to
    detect special sentences.
    """
    outlist = []
    ct = 0
    while len(batch) > 0:
        piece = batch.pop()
        if "[" not in piece and "]" not in piece:
            outlist.append(piece)
        else:
            frontpiece = piece.split("]")[0]
            inpiece = frontpiece.split("[")[1]
            inoptns = inpiece.split("|")
            for optn in inoptns:
                rebuild = frontpiece.split("[")[0] + optn
                rebuild += "]".join(piece.split("]")[1:])
                batch.append(rebuild)
    return outlist

def batchMatch(batch, match):
    t = False
    if isinstance(batch, str):
        batch = [batch]
    for piece in batchGen(batch):
        if piece.lower() in match.lower():
            t = True
    return t

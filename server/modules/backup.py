import json

SECURE = False # Verstößt gegen Punkt 2

def isValid(text):
    text = text.lower()
    if ('erstell' in text or 'mach' in text or 'sicher' in text) and ('backup' in text or 'speicher' in text or 'date' in text):
        return True
    else:
        return False

def check(thing):
    if type(thing) == type({'test':'test'}):
        thing = check_dict(thing)
    elif type(thing) == type(['test']):
        thing = check_list(thing)
    else:
        thing = str(thing)
    return thing

def check_list(liste):
    out = []
    for value in liste:
        try:
            x = json.dumps(value)
        except:
            value = check(value)
        out.append(value)
    return out

def check_dict(c_dict):
    o_dict = {}
    for key, value in c_dict.items():
        try:
            x = json.dumps(key)
        except:
            key = str(key)
        try:
            x = json.dumps(value)
        except:
            value = check(value)
        o_dict[key] = value
    return o_dict

def check_iter(iter):
    liste = []
    for value in iter:
        try:
            x = json.dumps(value)
        except:
            value = check(value)
        liste.append(value)
    liste = tuple(liste)
    return liste

def handle(text, luna, profile):
    luna.asynchronous_say('Okay, ich erstelle eine Kopie meiner temporären Daten.')
    backup_json = {}
    backup_json['Local_storage'] = check(profile)
    backup_json['Log_raw'] = check(luna.core.Log.log)

    with open(luna.path + '/LUNA_LOG.json','w') as json_file:
        json.dump(backup_json, json_file, indent=4, ensure_ascii=False)
    luna.say('Die Daten wurden gespeichert.')

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

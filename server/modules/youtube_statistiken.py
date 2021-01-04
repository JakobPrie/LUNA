from module_skills import get_text_beetween


def isValid(text):
    text = text.lower()
    if 'starte' in text and 'quiz' in text:
        return True
    else:
        return False


def handle(text, luna, profile):
    text = text.lower()
    if "wann" in text and 'hat' in text and 'hochgeladen' in text:
        t_split = text.split()
        index = get_index(text, "hat")
        correct_channel = False
        while not correct_channel:
            try:
                index += 1
                channel_name = t_split[index]

            except:
                continue


def get_index(text, start_word):
    index = -1
    text = text.split()
    for i in range(len(text)):
        if i == start_word:
            # Man könnte meinen, dass das Feld *nach* dem Wort das
            # richtige ist, also index = i+1, allerdibgs wird in dem
            # try zunächst der index um eins erhöht. Daher rechne
            # ich hier noch nicht eins auf den index drauf
            index = i

    return index
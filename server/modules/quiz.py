#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Jede Frage wird als dictionary gespeichert.
# Dabei muss bei "erste_ausgabe" angegeben werden,
# ob zunächst die Frage oder erst die Audio kommen
# soll. Dafür einfach "Frage", bzw. "Audio" ein-
# tragen. Mit Frage ist der zu sagende Text gemeint.
# Die Antwortmöglichkeiten sind optional.

# Zur einfacheren Handhabung wird der Audio-Pfad schon hier festgelegt
# und kann im dictionary einfach nur der Name der Audio-Datei angegeben
# werden. Diese Datei muss dann aber auch in den Ordner gespeichert werden
# !!!ACHTUNG!!! Bei den Audio-Dateien muss es sich um wav-Dateien handeln
import json
import random

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def isValid(text):
    return False

def handle(text, luna, profile):
    text = text.lower()
    AUDIO_PFAD = luna.path + "/modules/resources/Quiz/Audio"
    with open(luna.path + "/modules/resources/Quiz/questions.json", 'r') as question_file:
        FRAGEN = json.load(question_file)

    richtig = 0
    insgesamt = 0
    luna.say("Willkommen im Quiz! Wenn du keine Lust mehr hast, antworte auf eine Frage einfach mit 'Stopp' oder 'Abbruch'.")
    # Anschließend werden die richtigen Fragen "geladen"
    if 'über' in text or 'zu' in text:
        if 'allgemeinwissen' in text:
            possibilities = FRAGEN["allgemeinwissen"]
        elif 'geo' in text:
            possibilities = FRAGEN["geographie"]
        elif 'musik' in text:
            possibilities = FRAGEN["musik"]
    else:
        pos = ["allgemeinwissen", "geographie", "musik"]
        possibilities = FRAGEN[random.choice(pos)]

    # Da man leider nicht random.choice & dict.remove() auf dict-
    # ionarys anwenden kann, muss hier das ganze in eine Array
    # umgewandelt werden
    fragen = []
    for item in possibilities:
        fragen.append(possibilities.get(item))

    on_going = True
    while on_going and len(fragen) > 0:
        import random
        item = random.choice(fragen)

        if item["erste_ausgabe"] == "Frage":
            # checken wir mal, ob ein Text drinnen steht
            if item["Frage"] != "":
                luna.say(item["Frage"])
                # Scheinbar gibt es einen zu sagenden Text.
                # Wie sieht es mit der Audio aus?
                if item["Audio"] != "":
                    # Das doppelte Aufrufen ginge in der 3.9-Version von python besser,
                    # wir arbeiten aber leider mit der 3.4, bzw. 3.5. Vlt. sollte man
                    # irgendwann mal über ein Update nachdenken
                    try:
                        path = AUDIO_PFAD + item["Audio"]
                        luna.play(pfad=path)
                    except:
                        # WICHTIG: Wenn die Audio wichtig für die Frage ist, aber nicht im Ordner
                        # gefunden wird, wird der Text trotzdem gesagt. Es könnte keinen Sinn ergeben,
                        # Daher sagen wir es einfach dem Nutzer und überspringen die Frage
                        # scheinbar gibt es die Audio nicht.
                        luna.say("Leider gab es ein Problem beim Abspielen einer Audio-Datei. Daher machen wir einfach mit der nächsten Frage weiter!")
                        fragen.remove(item)
                        # ToDO Log-Eintrag schreiben
                        continue
                # Wenn es keine Audio gibt, einfach nichts machen. Eine Frage wurde ja schon gestellt...
                if item["Antwortmoeglichkeiten"] != [] and len(item["Antwortmoeglichkeiten"]) <= 26: # ich hoffe einfahc mal, dass letzteres zutrifft :)
                    moeglichkeiten = item["Antwortmoeglichkeiten"]
                    for i in range(len(item["Antwortmoeglichkeiten"])):
                        text = ALPHABET[i] + ": " + moeglichkeiten[i]
                        luna.say(text)
            else:
                # Man könnte natürlich noch überprüfen, ob es eine Audio
                # gibt und diese ggf. abspielen. Aber wenn nur ein Lied
                # abgespielt wird und die Frage "Wie heißt der Komponist"
                # wäre, bringt das dem Nutzer nichts. Also löchen
                # wir die Frage einfach aus der Liste, schreiben einen
                # Fehler in den Log und machen mit einer neuen weiter
                fragen.remove(item)
                # ToDO Log-Eintrag schreiben
                continue
        elif item["erste_ausgabe"] == "Audio":
            # selbes procedere wie bei der Textausgabe, daher
            # erspare ich mal allen die Kommentare. Bei Unklarheiten
            # einfach in das Pardon in der Textausgabe oben nachschauen
            if item["Audio"] != "":
                luna.play(pfad=item["Audio"])
                if item["Frage"] != "":
                    luna.say(item["Frage"])
            else:
                fragen.remove(item)
                # ToDO Log-Eintrag schreiben
                continue
        else:
            # Wenn kein Anfang angegeben wurde, könnte man natürlich
            # einfach gucken, ob Frage und/oder Audio angegeben wurde
            # und dann jeweilige sagen/abspielen, da das aber sehr
            # Fehleranfällig wäre, machen wir einfach das selbe wie
            # zuvor, wenn das Dictionary unvollständig war:
            fragen.remove(item)
            # ToDO Log-Eintrag schreiben
            continue

        user_response = " " + luna.listen().lower() + " "
        # Das Leerzeichen vor und hinter dem listen() wird
        # benötigt, damit später die Überprüfung einer Re-
        # aktion auf eine Antwortmöglichkeit überprüft werden kann
        if 'abbruch' in user_response or 'stopp' in user_response or ("ich" in user_response and "kein" in user_response and ("lust" in user_response or "bock" in user_response) or "spaß" in user_response):
            if insgesamt == 0:
                luna.say("Okay, Quiz beendet.")
            elif insgesamt == 1:
                beantwortung = "falsch"
                if richtig == 1:
                    beantwortung = "richtig"
                luna.say("Okay, Quiz beendet. Du hast eine Frage beantwortet, diese war {}.".format(beantwortung))
            else:
                luna.say("Okay, Quiz beendet. Du hast {} Fragen beantwortet, davon waren {}% richtig".format(insgesamt, round(richtig/insgesamt*100)))


            on_going = False
        else:
            # Erst hier wird die Frage zu den insgesamt gestellten dazugezählt, damit
            # wegen einem Fehler übersprungene Fragen nicht mitgezählt werden. Darüber
            # hinaus soll auch bei einem Abbruch die Frage nicht mitgezählt werden
            insgesamt += 1

            # Dann prüfen, ob evtl. auf eine Antwortmöglichkeit reagiert wurde
            anz_antwort = len(item["Antwortmoeglichkeiten"])
            valid = False
            while not valid:
                for i in range(len(ALPHABET)):
                    # Das ist nötig, da auch gesagt werden kann:
                    # "Ich glaube es ist a"
                    if " " + ALPHABET[i] + " " in user_response:
                        if i > anz_antwort-1:
                            luna.say("Ungültige Eingabe! Versuch es nocheinmal!")
                            user_response = " " + luna.listen().lower() + " "
                            break
                        else:
                            user_response = item["Antwortmoeglichkeiten"][i].lower()
                            print(f"GEFUNDEN --> {user_response}\n")
                            valid = True
                            break
                if len(user_response) > 0:
                    valid = True
                else:
                    luna.say("Bitte versuch es noch einmal.")
                    user_response = " " + luna.listen().lower() + " "

            # Es soll eine Wahrscheinlichkeit berechnet werden,
            # zu welcher die Antwort richtig ist.
            founded_parts = 0
            richtige_antwort = item["Antwort"].lower().split(" ")
            fragen.remove(item)
            max_parts = len(richtige_antwort)
            # Anschließend wird nach sehr einfacher (und wahrscheinlich
            # auch sehr fehleranfälliger) Logik die Wahrscheinlichkeit
            # berechnet, mit welcher die richtige Antwort genannt wurde
            for letter in richtige_antwort:
                # for letter in richtige_antwort und nicht for letter in user_response
                # ist wichtig für die Ermittlung der Wahrsheinlichkeit
                if letter.lower() in user_response:
                    founded_parts += 1
                elif letter.lower()[:-1] in user_response:
                    founded_parts += 1
                elif (letter.lower()+"s") in user_response:
                    founded_parts += 1

            prozentual = founded_parts / max_parts

            # Nun wird die Antwort auf die jeweilige Prozentzahl angepasst
            # Die Reihenfolge der ifs ist sehr wichtig, da sie entweder von
            # klein nach groß oder andersherum gehen muss, damit keine falschen
            # Ausgaben kommen. Also wenn dieser Part erweitert werden soll,
            # muss unbedingt auf das richige Einordnen geachtet werden!
            if prozentual >= 0.8:
                # Den alten Text brauchen wir nicht mehr, also kann er auch überschrieben werden
                text = random.choice(["Richtig!", "Das stimmt!", "Das ist richtig!"])
                richtig += 1
            elif prozentual >= 0.5:
                richtig += 1
                text = random.choice(["Das könnte stimmen.", "Ich bin mir nicht sicher, ob das richtig ist."])
                text += " Die richtige Antwort lautet wie folgt: " + item["Antwort"]
            elif prozentual >= 0.2: # hier bin ich mir nicht sicher, ob der Wert zu großzügig gewählt wurde. TESTEN!!!
                text = random.choice(["Das dürfte nicht stimmen.", "Ich glaube nicht, dass das richtig ist."])
                text += " Die richtige Antwort lautet wie folgt: " + item["Antwort"]
            else: # <= 0.2
                # Obwohl 20% richtig sind, müsste es falsch sein, da standartwörter wie 'und'
                # auch als richtig gewertet werden, aber in den meisten deutschen Sätzen vorkommen
                text = random.choice(["Das stimmt nicht. ", "Das ist leider falsch. ", ""])
                text += "Die richtige Antwort lautet wie folgt: " + item["Antwort"]
            luna.say(text)

    if len(fragen) == 0:
        luna.say("Scheinbar habe ich keine Fragen mehr zu diesem Thema.")
        luna.say("Du hast {} Fragen beantwortet, davon waren {}% richtig".format(insgesamt, round(
            richtig / insgesamt * 100)))

if __name__ == "__main__":
    class Luna:
        def __init__(self):
            self.local_storage = {}
            self.user = 'Baum'
            self.path = ".."
            self.analysis = {'room': 'None', 'time': {'month': '10', 'hour': '10', 'year': '2010', 'minute': '00', 'day': '09'}, 'town': 'None'}

        def say(self, text):
            print(text)
        def listen(self):
            neuertext = input()
            return neuertext

    def test():
        profile = {}
        luna = Luna()
        print("FRAGE eingeben")
        handle("starte quiz", luna, profile)

    test()
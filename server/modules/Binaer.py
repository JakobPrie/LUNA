#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
PRIORITY = -1
SECURE = True
import wikipedia
import re
wikipedia.set_lang("de")

"""
Was weißt du über <>
Was ist <>
Was sind <>
Wer war <>
Definiere mir <>
Was verstehst du unter <>
Weißt du etwas über <>
"""

def isValid(text):
    text = text.lower()
    ext = text.lower().replace("ß", "ss")
    batch = [
        "was weisst du über",
        "[was|wer] [ist|sind|war|waren]",
        ]
    if batchMatch(batch, text) or "was versteh" in text or "definier" in text:
        return True
    else:
        return False


def handle(text, luna, profile):
    text = text.lower().replace("ß", "ss")
    try:
        if "über" in text:
            article = text.split("über ")[1]
        elif "was ist" in text or "wer ist" in text or "wer war" in text or "was war" in text:
            article = text.split("ist ")[1] if len(text.split("ist ")) >= 2 else text.split(" war")[1]
        elif "was sind" in text or "wer sind" in text or "wer waren" in text or "was waren" in text:
            article = text.split("sind ")[1].rstrip("s") if len(text.split("ist ")) >= 2 else text.split(" waren")[1].rstrip("s")
        elif "was " in text  and (" ist" in text or " sind" in text):
            article = text.split("was ")[1].split(" ist")[0].split(" sind")[0].split(" war")[0].split(" waren")[0]
        elif "wer " in text  and (" ist" in text or " sind" in text):
            article = text.split("wer ")[1].split(" ist")[0].split(" sind")[0].split(" war")[0].split(" waren")[0]
        elif "unter" in text:
            article = text.split("unter ")[1]
        elif "definier" in text:
            article = " ".join(text.split("defi")[1].split(" ")[1:])
            article = masstrip(article, ["uns ", "mir ", "ihr ", "ihm "])
        else:
            article = "fehler"
        article = article.strip().strip("bitte")
        article = masstrip(article, ["ein ", "eine ", "einen ", "der ", "die ", "das ", " ist", " sind"])
        try:
            wikitext = wikipedia.summary(article)
            wikitext = shorten(wikitext)
            luna.say("Ich habe folgendes herausgefunden: " + wikitext)
        except wikipedia.exceptions.DisambiguationError as e:
            succ = False
            for el in e.options:
                if succ is True:
                    break
                next = el.strip()
                try:
                    wikitext = wikipedia.summary(next)
                    wikitext = shorten(wikitext)
                    outstr = "Leider bin ich mir nicht ganz sicher, was du mit dem Begriff " + article + " meintest. "
                    outstr += "Am ehesten passte für mich der Begriff " + next + ", den ich deshalb für dich beschreibe. "
                    outstr += wikitext
                    succ = True
                except wikipedia.exceptions.DisambiguationError as ef:
                    print("EEERRR", ef)
                    outstr = "Leider kann ich dir im Moment nichts darüber erzählen. vielleicht versuchst du, deine Frage klarer zu formulieren?"
                except wikipedia.exceptions.PageError:
                    luna.say("Ich habe zwar Antworten gefunden, aber keine davon passt so richtig auf deine Frage. Entschuldige.")
            luna.say(outstr)
        except wikipedia.exceptions.PageError:
            luna.say("Leider weiß ich keine Antwort auf deine Frage. Vielleicht hilft dir eine Suche im Internet weiter?")
    except IndexError:
        luna.say("Leider hast du deine Frage so forumliert, dass ich sie nicht verstehen konnte. Das tut mir leid, versuch s doch einfach erneut!")

## WIKIPEDIA-extract first sentence

def shorten(long):
    short = ""
    for block in long.split(")"):
        short += block.split("(")[0]
    cutsen = 1
    output = ""
    while cutsen <= 5:
        t_output = ". ".join(short.split(".")[0:cutsen]) + "."
        if len(t_output) <= 130 or t_output[-2] in "0123456789":
            cutsen += 1
        else:
            output = t_output
            cutsen = 10
        cutsen += 1
    output = output.replace("  ", " ").replace("..",".").replace(". .", ".").replace(" ,", ",").replace(" . ", ". ")
    return output

def masstrip(input, blacklist):
    for word in blacklist:
        input = input.replace(word, "")
    return input.strip()

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

import subprocess

SECURE = False # Verstößt gegen Punkt 1
PRIORITY = -1

# Nutzt das fortunes-de package verfügbar auf debian und ubuntu.
# Das paket stellt irgendwelche sätze oder zitate bereit.
# Das Modul wird nur aktiv, wenn `fortunes-de` installiert ist.

def isValid(text):
    if ('erzähl' in text.lower() or 'sag' in text.lower()) and ('irgendwas' in text.lower() or 'irgendetwas' in text.lower() or 'etwas' in text or 'was' in text):
        try:
            installedStr = subprocess.check_output("dpkg-query --show --showformat='${db:Status-Status}\n' 'fortunes-de'", shell=True).decode('utf-8').lower()
            if 'installed' in installedStr and 'not' not in installedStr:
                return True
        except subprocess.CalledProcessError:
            return False
    return False

def handle(text, luna, profile):
    try:
        fortune = subprocess.check_output("fortune", shell=True).decode('utf-8').strip().lower()
        if (fortune != ''):
            luna.say(fortune)
        elif 'irgendetwas' in text.lower():
            luna.say('irgendetwas')
        else:
            luna.say('irgendwas')
    except subprocess.CalledProcessError:
        if 'irgendetwas' in text.lower():
            luna.say('irgendetwas')
        else:
            luna.say('irgendwas')

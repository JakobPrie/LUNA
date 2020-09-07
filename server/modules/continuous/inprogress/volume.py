import datetime
import subprocess

INTERVALL = 3600

def run(luna, profile):
    now = datetime.datetime.now()
    endeUhrzeit = datetime.datetime(22, 00)
    if now == endeUhrzeit:
		befehl = "amixer  sset PCM1,0 100%"
		subprocess.Popen([befehl.split(" ")])

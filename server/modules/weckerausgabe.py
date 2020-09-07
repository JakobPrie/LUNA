import os

SECURE = True # Damit es von fortlaufenden module naufgerufen werden kann

def handle(text, luna, profile):
    user = text.get('Benutzer')
    text = text.get('Text')
    path = "/home/pi/Desktop/LUNA/server/modules/resources/aufstehen.wav"
    
    luna.say(text, user=user)
    play(path, luna)
    
def play(pfad, luna):
    try:
        chunk = 1024
        
        format = {'format': 8,
                  'channels':1,
                  'rate':88200,
                  'chunk':chunk}
        wav = wave.open(pfad, 'rb')
        wav_data = wav.readframes(chunk)
        audio_buffer = []
        while wav_data:
            audio_buffer.append(wav_data)
            wav_data = wav.readframes(chunk)
        audio_buffer.append('Endederdurchsage')
        luna.audio_Output.playback_audio_format = format
        luna.audio_Output.play(audio_buffer)
        
    except Exception as e:
        print(f"Abbruch durch Fehler: {e}")
        

def isValid(text):
    return False

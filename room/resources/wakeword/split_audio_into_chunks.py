import os
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks

def main(args):
    def chunk_and_save(file):
        audio = AudioSegment.from_file(file)
        length = args.seconds * 1000 # this is in milliseconds
        chunks = make_chunks(audio, length)
        names = []
        for i, chunk in enumerate(chunks):
            _name = file.split("/")[-1]
            names = "{}_{}".format(i, _name)
            wav_path = os.path.join(args.save_path, names)
            chunk.export(wav_path, format="wav")
        return names

    chunk_and_save(args.audio_file_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="script to split audio files into chunks")
    parser.add_argument('--seconds', type=int, default=None, help='wenn auf None gesetzt, wird bis zu einem keyboard interrupt aufgenommen')
    parser.add_argument('--audio_file_name', type=str, default=None, required=True, help='Name der Audio-Datei')
    parser.add_argument('--save_path', type=str, default=None, required=True, help='absoluter Pfad zu den zu speichernden Dateien')
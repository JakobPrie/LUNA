#!/usr/bin/pythob
#-*- coding:utf-8 -*-

#Modul schickt ein Youtube-Video, das als url übergeben wird an Telegram.
#Daher nur für Telegram vorgesehen

import pytube
import os
import traceback

def isValid(text):
	text = text.lower()
	
	if 'schicke' in text or 'schick' in text or 'sende' in text and 'video' in text and not 'einkaufsliste' in text:
		return True
	if 'lade' in text and 'youtubevideo' in text and 'herunter' in text:
		return True

	
def handle(text, luna, profile):
	print(luna.path)
	SAVE_PATH = luna.path + '/modules/resources'
	VIDEO_PATH = SAVE_PATH + '/YouTube.mp4'
	luna.say('Wie lautet die URL von dem Youtube-Video, das ich dir schicken soll?', output='telegram')
	response = luna.listen(input='telegram')
	try:
		luna.say('Video wird heruntergeladen. Bitte warte einen Moment.', output='telegram')
		try:
			youtube = pytube.YouTube(response)
		except:
			luna.say('Der Link konnte keinem Video zugeordnet werden.')
		
		video = youtube.streams.get_highest_resolution()
		print(video)
		video.download(SAVE_PATH, filename="YouTube")
		print('Video heruntergeladen.')
		
		send_video_to_telegram(luna, VIDEO_PATH)
	
	except Exception as e:
		print(f"Abbruch durch Fehler: {e}")
		luna.say('Es gab einen Fehler. Bitte versuche es erneut.')
		traceback.print_exc()
	try:
		os.remove(VIDEO_PATH)
		print('Video gelöscht')
	except:
		print('Video konnte nicht gelöscht werden.')
		traceback.print_exc()
		print('Klasse abgeschlossen')
	print(pytube.exceptions.PytubeError)
		
def send_video_to_telegram(luna, VIDEO_PATH):
	print(VIDEO_PATH)
	try:
		uid = luna.local_storage['LUNA_telegram_name_to_id_table'][luna.user]
		luna.telegram.bot.send_file(uid, video=open(VIDEO_PATH, 'rb'), supports_streaming=True)
	except KeyError as e:
		Log.write('WARNING', 'Der Text "{}" konnte nicht gesendet werden, da für den Nutzer "{}" keine Telegram-ID angegeben wurde'.format(text, user), conv_id=original_command, show=True)
		print(f"Abbruch durch Fehler: {e}")
		traceback.print_exc()
		print(pytube.exceptions.PytubeError)

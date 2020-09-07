
def isValid(text):
	text = text.lower()
	if 'module' in text and 'fehlerhaft' in text:
		return True
	elif 'module' in text and 'funktionieren' in text and 'nicht' in text:
		return True

def handle(text, luna, profile):
	faulty_list = []
	for module in luna.local_storage['modules'].values():
		if module['status'] == 'error':
			faulty_list.append(module['name'])
	print(faulty_list)
	luna.say('Folgende Module konnten nicht geladen werden: ')
	luna.say(luna.enumerate(faulty_list))
	


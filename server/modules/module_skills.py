def isValid(text):
	return False

def handle(text, luna, profile):
	pass

def get_enumerate(array):
	# print(array)
	new_array = [] # array=['Apfel', 'Birne', 'Gemüse', 'wiederlich']
	for item in array:
		new_array.append(item.strip(' '))
		
	# print(new_array)
	ausgabe = ''
	# print('Länge: {}'.format(len(new_array)))
	if len(new_array) == 0:
		pass
	elif len(new_array) == 1:
		ausgabe = array[0]
	else:
		for item in range(len(new_array) - 1):
			ausgabe += new_array[item] + ', '
		ausgabe = ausgabe.rsplit(', ', 1)[0]
		ausgabe = ausgabe + ' und ' + new_array[-1]
	return ausgabe

def correct_output(luna_array, telegram_array):
	if luna.telegram_call is True:
		return telegram_array
	else:
		return luna_array

def get_text_beetween(start_word, text, end_word='', output='array'):
	ausgabe = []
	index = -1
	text = text.split(' ')
	for i in range(len(text)):
		if text[i] is start_word:
			index = i+1
	if index is not -1:
		if end_word is '':
			while index <= len(text):
				ausgabe.append(text[index])
				index += 1
		else:
			founded = False
			while index <= len(text) and not founded:
				if text[index] is end_word:
					founded = True
				else:
					ausgabe.append(text[index])
					index += 1
	if output is 'array':
		return ausgabe
	elif output is 'String':
		ausgabe_neu = ''
		for item in ausgabe:
			ausgabe += item + ' '
		return ausgabe

def open_more_times(user=None, name=None, text=None, room=None, count=3):
	room = self.room
	new_text = str(text)
	new_text = new_text.replace('paar ', '') # super wichtig, da sonst ein loop generiert wird
	new_text = new_text.replace(str(count), '') 
	if user == None:
		user = self.user
	for i in range(count):
		luna.start_module(user, name, text, room)
		
def delete_duplications(array):
	new_array =list(set(array))
	return new_array

def assamble_new_items(array, new_items):
	for item in array:
		if item in new_items:
			anz = item.split(' ', 1)[0]
			last_letter= item[-1]
			if type(anz) is int:
				new_anz = int(anz) + n_anz
				item = str(new_anz) + anz[1]
				if last_letter is "e":
					item = item + "n"
			else:
				item = "2 " + item
				if last_letter is "e":
					item = item + "n"
	return array
				

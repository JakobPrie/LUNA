import datetime

def isValid(text):
	text = text.lower()
	if 'ist' in text and 'schaltjahr' in text:
		return True
	elif 'wann' in text and 'schaltjahr' in text:
		return True
		
def handle(text, luna, profile):
	if 'wann' in text and ('nächste' in text or 'wieder' in text):
		year = datetime.date.today().year
		founded = False
		while founded is False:
			if leap_year(year) is True:
				luna.say('Das nächste Schaltjahr ist {}'.format(year))
			else:
				year += 1
	elif 'ist' in text and 'schaltjahr' in text:
		ist_schaltjahr = leap_year(get_year(text))
		output = 'eventuell ein'
		if ist_schaltjahr is True:
			output = 'ein'
		else:
			output = 'kein'
		luna.say('Das Jahr {} ist {} Schaltjahr.'.format(get_year(text), output))
	

def get_year(text):
	year = -1
	text = text.split(' ')
	for item in text:
		try:
			year = int(item)
		except ValueError:
			pass
	
	return year
	

def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
        

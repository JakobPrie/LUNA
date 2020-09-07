from phue import Bridge


def isValid(text):
	text = text.lower()
	if 'xy' in text and 'farbe' in text:
		return True
		
def handle(text, luna, profile):
	bridge = Bridge('192.168.178.85')

	xy = bridge.get_light(1, 'xy')
	print('XY: {}'.format(xy))


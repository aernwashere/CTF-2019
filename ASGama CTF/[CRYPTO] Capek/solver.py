w = open('base.dms','r').read()
from base64 import *

c = w
while True:
	try:
		try:
			c = b64decode(c)
		except:
			c = b32decode(c)
	except:
		print c
		break

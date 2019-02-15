import base64

enc = open('TryFlag','r').read()

flag = "KSL{"

loop = True

while (loop):
	enc = base64.b64decode(enc)
	if flag in enc:
		loop = False

print (enc)

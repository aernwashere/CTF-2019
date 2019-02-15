import base64

def decrypt(enc,key):

	enc = base64.b64decode(enc)

	dec = ""
	
	for i in range(len(enc)/len(key)):
		for j in range(len(key)):
			dec += chr((ord(enc[i * len(key) + j]) ^ ord(key[j])) % 256)

	return (dec)

if __name__ == "__main__":

	encrypted = open('encrypted','r').read()
	key = "KaEsEl"
	
	plaintext = decrypt(encrypted,key)
	print(plaintext)

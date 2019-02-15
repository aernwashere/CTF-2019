import base64

def encrypt(plaintext,key):
	enc = ""
	
	for i in range(len(plaintext)/len(key)):
		for j in range(len(key)):
			enc += chr((ord(plaintext[i * len(key) + j]) ^ ord(key[j])) % 256)

	enc = base64.b64encode(enc)

	return (enc)

if __name__ == "__main__":

	flag = "---REDACTED---"
	key = "KaEsEl"
	
	encrypted = encrypt(flag,key)
	print(encrypted)

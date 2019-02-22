import string, os, random, time, binascii
from Crypto.Cipher import AES

def generate_random(n):
    return (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n)))

filectime = 1543422121

data = open('flag?.pdf.pie','rb').read()

#tes = open('test.txt','rb').read()

random.seed(filectime)
key = generate_random(16)
iv = generate_random(16)

newkey = key.encode("utf-8").encode('hex')
newiv = iv.encode("utf-8").encode('hex')

#key = "6gf5ady22oc3sed2"
#iv = "jhlse0idscl608hr"

key = "6gf5ady22oc3sed2"
iv = "jhlse0idscl608hr"

aes = AES.new(key, AES.MODE_CBC, iv)
dec = aes.decrypt(data)

#aess = AES.new(key,AES.MODE_CBC, iv)
#enc = aess.encrypt(tes)

#w = open('test.txt.enc', 'wb').write(enc)

w = open('flag.pdf', 'wb').write(dec)

print ("ok")

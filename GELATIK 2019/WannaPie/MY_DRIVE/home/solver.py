import string, os, random, time, binascii
from Crypto.Cipher import AES

def generate_random(N):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

data = open("exam.pdf.pie", 'rb').read()

atime_epoch = 1552669684
mtime_epoch = 1550411198
ctime_epoch = 1552640883

random.seed(int(ctime_epoch))

key = generate_random(16)
iv = generate_random(16)

key = "2fbiuo3m6jyulbnf"
iv = "sazzzp8sn6fp1bkd"

aes = AES.new(key, AES.MODE_CBC, iv)
dec = aes.decrypt(data)

d = open("exam.pdf", 'wb').write(dec)

print ("ok")

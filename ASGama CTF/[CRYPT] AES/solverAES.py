from pwn import *
from Crypto.Cipher import AES
import binascii

r = remote("asgama.web.id", 42002)

r.recvuntil("rahasia : ")
kode_rahasia = r.recvline()[:-1]
print "kode rahasia : " + kode_rahasia

r.recvuntil("menjadi : ")
target = r.recvline()[:-1]
print "target       : " + target
r.recvuntil("hex) : ")
data = r.recvline()[:-1].split()
cipher = data[0]
iv = data[4]
print "iv           : " + iv
print "cipher       : " + cipher
newiv = ''

for i in range(len(target)):
	p = (ord(kode_rahasia[i:i+1]) ^ ord(iv[i:i+1]))
	q = (p ^ ord(target[i:i+1]))
	print q
	newiv += chr(q)

print newiv
print len(newiv)

print r.recvuntil(">>> ")
r.sendline("2")

print r.recvuntil(" : ")
r.sendline(newiv)



print r.recv()

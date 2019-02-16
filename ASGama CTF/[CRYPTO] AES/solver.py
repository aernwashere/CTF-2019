from pwn import *

r = remote('asgama.web.id', 42002)

r.recvuntil('Pak Gege ingin mengirim kode rahasia : ')
kode_rahasia = (r.recvline().split())[0]
r.recvuntil('Bagaimana cara Pak Setiawan mengganti hasil dekripsi menjadi : ')
target = (r.recvline().split())[0]
r.recvuntil('Sementara Ciphernya(encoded hex) : ')
cipher, _, _, _, iv = r.recvline().split()

print "kode rahasia : " + kode_rahasia
print "target       : " + target
print "cipher       : " + cipher
print "iv           : " + iv

x = []
for i in range(len(iv)):
    x.append(ord(iv[i]) ^ ord(kode_rahasia[i]))

new_iv = []
for i in range(len(x)):
    new_iv.append(x[i] ^ ord(target[i]))

lol = ''.join(chr(a) for a in new_iv)

r.recvuntil('>>> ')
r.sendline("2")
r.recvuntil('Masukan IV : ')
r.sendline(lol)
print r.recv()

from pwn import *

r = remote('asgama.web.id', 40501)
#r = process(['','noah','stripped.dms'])
#print r.recv()


a1 = ['A'] * 20
v2 = 1
v3 = 0

for i in range(20):
    if (i % 5):
        v3 += ord(a1[i])
    else:
        v2 *= ord(a1[i])
print ''.join(a1)
print v2 - v3

r.recvuntil('Pass : ')
r.sendline(''.join(a1))
r.recvuntil('ID : ')
r.sendline(str(v2-v3))
print r.recv()

from pwn import *
cigam = 'mbO`^Ifco^DfifPqf@buMf^iFal@flRqQr'
magic = '''
 0C0h, 0C3h, 0C1h, 0C2h, 0D8h, 57h, 50h, 90h, 90h, 90h, 90h,
 0D8h, 57h, 53h, 90h, 90h, 90h, 90h, 0D8h, 57h, 51h, 90h, 90h, 90h, 90h,
 0D8h, 57h, 52h, 90h, 90h, 90h, 90h, 1Ah, 8Ch, 97h, 0D8h, 6Fh
 50h, 14h, 4Bh, 0E5h, 66h, 0D8h, 6Fh, 58h, 29h, 0F4h
 90h, 90h, 90h, 0FAh, 90h, 19h, 94h, 0B4h, 1Ah, 87h, 18h
 0C4h, 0B4h, 94h, 2Bh, 90h, 90h, 90h, 90h, 7Bh, 88h, 0D8h, 1Dh
 94h, 8Fh, 1Ah, 80h, 18h, 0C4h, 0B4h, 96h, 1Ah, 0C4h
 0B4h, 94h, 18h, 80h, 1Ah, 0C4h, 0B4h, 96h, 18h, 0C4h
 0B4h, 94h, 6Fh, 53h, 0ABh, 8Ch, 0B4h, 0E5h, 71h, 18h
 87h, 0D8h, 6Fh, 5Bh, 0D8h, 1Dh, 84h, 8Fh, 0F6h, 1Bh
 92h, 0F6h, 6Fh, 58h, 0F6h, 19h, 92h, 6Fh, 59h, 15h
 59h, 0E5h, 2Ch, 0D8h, 13h, 54h, 98h, 0CAh, 0C9h, 0CBh
 0C8h, 53h,
'''
magic = magic.replace(' ','0x')
magic = magic.replace(',','')
magic = magic.replace('h',' ')
magic = magic.split()
magic = [eval(x) for x in magic]
print len(magic)
result = []
for i in magic:
    result.append(i ^ 144)
no = [ord(x) for x in cigam]

real = []
real.append(no[len(no)-2])
real.append(no[len(no)-1])
for i in range(len(no)-2):
    real.append(no[i])

for i in range(len(real)):
    real[i] += 3
real[0] -= 1
real[len(real)-1] -= 1

magicword = ''.join(chr(x) for x in real)

r = remote('asgama.web.id', 40502)
r.recvuntil('>>')
r.sendline(magicword)
print r.recv()

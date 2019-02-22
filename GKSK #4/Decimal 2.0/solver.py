flag = '''
 0Eh, 17h, 1Dh, 14h, 42h, 0Fh, 3Ch, 0FCh, 17h, 40h, 39h
 28h, 1Eh, 0FDh, 3Eh, 31h, 26h, 1Eh, 0FDh, 1Fh, 2Ch
 3Eh, 3Dh, 2Eh, 2Ch, 31h, 29h, 0FAh, 1Ah, 2Bh, 11h, 38h
 36h, 0FCh, 0Eh, 46h
'''
flag = flag.replace(' ', '0x')
flag = flag.replace(',',' ')
flag = flag.replace('h','')
flag = flag.split()
nflag = []
for i in flag:
    nflag.append(eval(i))
newf = [chr(x) for x in nflag]

pat = "GKSK"
key = ['9','4','6','7']
nkey = []
for x in key:
    nkey.append(ord(x))

ff = ''
for i in range(len(nflag)):
    ff += chr((nflag[i] + nkey[i%4])%256)

print ff

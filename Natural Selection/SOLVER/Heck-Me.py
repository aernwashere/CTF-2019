import binascii

enc = open('flag.enc','r').read()

print (binascii.unhexlify(enc))
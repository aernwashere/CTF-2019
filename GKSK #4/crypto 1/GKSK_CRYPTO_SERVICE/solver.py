secret_out = ''
from base64 import *

secret_str = ''.join('gksk-secret-code'.split('-'))
for count,loop in enumerate(secret_str):
    if count % 2 == 0:
        secret_out += ''.join([chr(ord(ch) + 0x3) for ch in loop])
    else:
        secret_out += loop
print "secret   : " +  secret_out

enc = open('flag.enc','r').read()
pattern = "GKSK{"
shift = 0
while True:
    shift += 1
    ciphertext = b64decode(enc)
    alphabet = secret_out * 50
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    flag = ''
    for i in range(len(ciphertext[:-1])):
        flag += chr((ord(ciphertext[i]) ^ shift) - ord(shifted_alphabet[i]))

    print flag
    if pattern in flag:
        break

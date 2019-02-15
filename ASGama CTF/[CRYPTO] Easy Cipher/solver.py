enc = open('encrypted.txt','r').read()
key = "Qk3j4cnmb8"
pattern = "GamaCTF{"
c = []

for i in range(len(enc)/2):
    k = '0x' + enc[i*2:i*2+2]
    c.append(eval(k))

flag = ""

for i in range(len(c)/len(key)):
    j = i
    for a in range(len(key)):
        flag += chr(c[j] ^ ord(key[a]))
        j += len(c)/len(key)

print flag

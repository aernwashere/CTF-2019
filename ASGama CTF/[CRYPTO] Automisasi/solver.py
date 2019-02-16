flag = "GamaCTF"
msg = open('encrypted.dms','r').read()
while True:
    for a in range(32,127):
        c = chr(a)
        f = flag + c
        cipher = ''
        for x in range(len(f)):
            for y in range(x):
                for z in range(y):
                    cipher += str(ord(f[z]) + ord(f[x]) - ord (f[y]))
        if msg[0:len(cipher)] == cipher:
            flag += c
            print flag
            break
    if cipher == msg:
        print "flag >> " + flag
        break
    elif len(cipher) > len(msg):
        print "not match"
        break


c =  "e7c1cdc1e3f4e6dbcfcec5ffc2d9d4c5ffd8cfd2d29f9fdd"
c = c.decode('hex')

pattern = "Gama"
flag = ''
k = 1
while True:
    for i in c:
        flag += chr(ord(i) ^ k)
    k += 1
    if pattern in flag:
        print flag
        break
    else:
        flag = ''

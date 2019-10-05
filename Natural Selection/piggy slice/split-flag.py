combined = open('panca.png', 'rb').read()
signature = combined[-8:]
flag = []
for i in range(4):
    s = 0
    tmp1 = ''
    tmp2 = ''
    while (tmp1[-8:] != signature) and (tmp2[-8:] != signature) and s < len(combined):
        if s % 2 == 1:
            tmp1 += combined[s]
        else:
            tmp2 += combined[s]
        s += 1
    if tmp1[-8:] == signature:
        flag.append(tmp1)
        combined = tmp2 + combined[s:len(combined)]
    if tmp2[-8:] == signature:
        flag.append(tmp1 + combined[s:len(combined)])
        combined = tmp2
flag.append(combined)

for i in range(4, -1, -1):
    open('image-flag-'+str(5 - i)+'.png', 'wb').write(flag[i])

print "Image sliced!"

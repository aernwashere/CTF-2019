img = []

for i in range(4):
    img.append(open('source/flag_0'+str(i+2)+'.png', 'rb').read())

tmp = open('source/flag_01.png', 'rb').read()

for i in range(4):
    if(len(tmp)>len(img[i])):
        k = len(tmp)
    else:
        k = len(img[i])

    new = ''
    for l in range(k):
        if l < len(tmp):
            new += tmp[l]
        if l < len(img[i]):
            new += img[i][l]
    open('panca.png', 'wb').write(new)
    tmp = open('panca.png', 'rb').read()
    
print "Image combined!" 

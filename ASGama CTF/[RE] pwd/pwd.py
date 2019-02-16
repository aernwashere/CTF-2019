text = [chr(x) for x in range(32,127)]
pwd = []
for i in text:
    for j in text:
        for k in text:
            for l in text:
                for m in text:
                    tmp = i+j+k+l+m
                    pwd.append(tmp)
                    print tmp
w = open('pwd.txt','w').write(pwd)

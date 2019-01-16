from pwn import *

r = remote("asgama.web.id", 40500)

print r.recvline()[:-1]
i = 0
while True:
    x = r.recv()
    try:
        x = int(x)
    except:
        print x
        break

    print "in " + str(x)

    if x > 255:
        dd = 2 
        while (x / dd > 100 or x % dd != 0):
            dd += 1

        if dd > 255:
            dd = 2

        data = chr(x / dd) + chr(dd)
    else:
        data = chr(x) + chr(1)

    r.sendline(data)
    print "out " + data
    i += 1
    print "       >>>>>>  " + str(i)

print r.recvline()

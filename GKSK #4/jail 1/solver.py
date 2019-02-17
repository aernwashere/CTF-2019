d = "system('ls')"
d = "system('cat flag.txt')"
key = ''
key += ''.join(str(ord(i)) + ".chr+" for i in d)
key = "eval(" + key[:-1] + ")"
print key[::-1]

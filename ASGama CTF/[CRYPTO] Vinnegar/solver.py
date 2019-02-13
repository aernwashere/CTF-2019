key = "milo".upper()
cip = "Qa_vsbiw_autz_kwev".upper()
flag = ""
j = 0
for i in range(len(cip)):
	d = ord(cip[i])
	if d in range(65,91):
		flag += chr((d - (ord(key[j%len(key)]))) % 26 + ord('A'))
		j += 1
	else:
		flag += chr(d)
print flag.lower()

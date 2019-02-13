w = open('desc','r').read()

flag = ""
for a in w:
	i = ord(a)
	if i >= ord('A') and i <= ord('Z'):
		i -= ord('A')
		i = (i + 5) % 26
		flag += chr(i + ord('A'))	
	elif i >= ord('a') and i <= ord('z'):
		i -= ord('a')
		i = (i + 5) % 26
		flag += chr(i + ord('a'))
	
	else:
		flag += chr(i)


print flag

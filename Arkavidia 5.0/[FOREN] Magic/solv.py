file = open ("megic.png", "rb").read()
key = "arvy"
tex = ""
it = 0
for i in file:
	tex += chr(ord(i) ^ ord(key[it]))
	it = (it + 1) % len(key)
with open ("flag.png", "wb") as out:
	out.write(tex)

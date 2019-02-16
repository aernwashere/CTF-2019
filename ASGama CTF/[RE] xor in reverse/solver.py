s = "a)))KkFmQ*wFz)TixK*||"

flag = ''
for i in s:
    flag += chr(ord(i) ^ 25)

print flag

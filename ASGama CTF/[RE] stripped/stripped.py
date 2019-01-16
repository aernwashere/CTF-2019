a = "96431297995810561790"
print "Pass : " + ''.join(str(x) for x in a)

v2 = 1
v3 = 0

for i in range(20):
    if i % 5:
        v3 += ord(a[i])
    else:
        v2 *= ord(a[i])

print v2-v3

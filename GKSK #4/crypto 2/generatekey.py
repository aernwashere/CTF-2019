import string, os, random, time, binascii

def generate_random(n):
    return (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n)))

filectime = 1547488463
random.seed(filectime)
key = generate_random(16)
iv = generate_random(16)

print (key)
print (iv)

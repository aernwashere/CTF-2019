import base64

enc = open('encrypted','r').read()


print(base64.b32decode(base64.b64decode(enc)))

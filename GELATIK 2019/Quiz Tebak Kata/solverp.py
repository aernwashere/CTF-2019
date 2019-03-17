from pwn import *
from base64 import *
from PIL import Image
r = remote("180.250.7.183", 7007)
while True:
    try:
        r.recvuntil(" text berikut:")
        txt1 = r.recv()
        txt2 = r.recvuntil("dalam")[:-6]

        txt = txt1 + txt2

        img = b64decode(txt)

        d = open("img.png", 'wb').write(img)

        image_obj = Image.open("img.png")
        rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save("next.png")

        import os
        import tempfile
        import subprocess

        def ocr(path):
            temp = tempfile.NamedTemporaryFile(delete=False)

            process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.communicate()

            with open(temp.name + '.txt', 'r') as handle:
                contents = handle.read()

            os.remove(temp.name + '.txt')
            os.remove(temp.name)

            return contents

        str = ocr('next.png')
        x = (str[:-2])
        print x

        r.sendline(x)
    except:
        print r.recv()
        break

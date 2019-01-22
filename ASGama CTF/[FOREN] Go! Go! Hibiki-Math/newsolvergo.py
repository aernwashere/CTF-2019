from pwn import *
from PIL import Image
from pyzbar import pyzbar
from cv2 import *

r = remote("asgama.web.id",40400)

for z in range(20):
    print r.recvuntil("Given an operation below : ")
    data = r.recvuntil("  Your answer : ")

    qr = data[1:-18]
    print qr
    qr = qr[1:].replace("\n ","")
    qr = qr.replace("\n","")

    if len(qr) == 1806:
        img = Image.new('RGB',(43,42))
        pix = img.load()
        it = 0
        for i in range(21):
            for j in range(43):
                if qr[it] == 'U':
                    a1 = 1
                else:
                    a1 = 0
                if qr[it+903] == 'U':
                    a2 = 1
                else:
                    a2 = 0

                if a1 ^ a2:
                    pix[j,i*2] = (255,255,255)
                    pix[j,i*2+1] = (255,255,255)
                it += 1

        img.save('qr.png')

    else:
        img = Image.new('RGB',(43,42))
        pix = img.load()
        it = 0
        if qr[it] == 'U':
            for i in range(21):
                for j in range(43):
                    if qr[it] != 'U':
                        pix[j,i*2] = (255,255,255)
                        pix[j,i*2+1] = (255,255,255)
                    it += 1

        else:
            for i in range(21):
                for j in range(43):
                    if qr[it] == 'U':
                        pix[j,i*2] = (255,255,255)
                        pix[j,i*2+1] = (255,255,255)
                    it += 1

        img.save('qr.png')

    im = imread('qr.png')
    qrread = pyzbar.decode(im)
    hibiki = qrread[0].data

    print hibiki
    data = eval(hibiki[:-1])
    print data
    r.sendline(str(data))

print r.recv()

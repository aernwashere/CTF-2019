from PIL import Image
from binascii import *

ok = ""
for i in range(1,626):
	name = "um_" + str(i) + ".jpg"
	img = Image.open(name)
	pix = img.load()
	color = pix[0,0]
	if (color == (255,255,255)):
      		ok += "1"
    	else: 
      		ok += "0"

img = Image.new('RGB',(25,25))

pixels = img.load()
it = 0
for i in range(25):
	for j in range(25):
		if(ok[it]=='1'):
			pixels[j,i] = (255,255,255)
		it += 1
img.save('out_um.jpg')


d = open("soal3.png", "rb").read()

l = 31 * 16

c = d[l:]
i1 = ""
i2 = ""
for i in range(1,len(c)):
    if i % 2 == 0 :
        i2 += c[i]
    else :
        i1 += c[i]

e = open("soal3_1.jpg","wb").write(i1)
e = open("soal3_2.jpg","wb").write(i2)

import sys
from PIL import Image

images = map(Image.open, ['soal3_1.jpg', 'soal3_2.jpg'])
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('flag.jpg')


print "ok"

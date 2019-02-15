from PIL import Image
import binascii

# Decrypter

im = Image.open("checkME.png")

biyte = ""
pixels = img.load()
for row in range(im.height):
  for col in range(im.width):
    color = pixels[col,row]
    if (color == (255,255,255)):
      biyte+="0"
    else: 
      biyte+="1"

print (biyte)
print ("\nDecode this binary at http://tomeko.net/online_tools/bin_decoder.php?lang=en")

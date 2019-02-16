c = """
 0AAh, 0E5h, 8Dh, 0B1h, 0BFh, 0EAh, 0DEh, 0CDh, 0B9h
 0DFh, 0ACh, 0C9h, 0E1h, 0DFh, 9Ch, 81h, 0F9h, 8Eh, 81h
 0A0h, 0B1h, 9Dh, 0D1h, 0A1h, 0B0h, 0ADh, 0E5h, 8Eh
 9Ch, 0BBh
"""
c = c.replace(' ', '0x')
c = c.replace(',',' ')
c = c.replace('h','')
c = c.split()

pwd = [0xde,0xad,0xbe,0xee,0xef]

flag = [int(x,16) for x in c]
msg = ''
for i in range(len(flag)):
    msg += chr(flag[i] ^ pwd[i%5])

print msg

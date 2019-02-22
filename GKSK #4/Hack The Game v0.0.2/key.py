"nc 180.250.7.183 20202"
key = "GKSK{4re_Y0u_53ri0usly_checking_f0r_b3t4_t3sT?}"
import string
from base64 import *

code = "PlayerLevel=1;PlayerExp=1;PlayerHP=100;PlayerAtk=987654321;PlayerDef=987654321;PlayerName=ar"
enhace =  b64encode(code)

text = "abcdefghijklmnopqrstuvwxyz"

rest = "ugXHEwvYtgv2zwW9mtTqBgf5zxjfEha9mdTqBgf5zxjiud0Xmda7ugXHEwvYqxrRpteWo1bSyxLLCKrLzJ01o1bSyxLLCK5HBwu9yxi="

reveal = ''
for i in enhace:
    if i in text.upper():
        reveal += i.lower()
    elif i in text.lower():
        reveal += i.upper()
    else:
        reveal += i

print reveal

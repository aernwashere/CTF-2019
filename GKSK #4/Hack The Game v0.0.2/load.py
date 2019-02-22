from base64 import *

code = "PlayerLevel=1;PlayerExp=1;PlayerHP=100;PlayerAtk=987654321;PlayerDef=987654321;PlayerName=ar"
enhace =  b64encode(code)

print enhace

#!/usr/bin/python
# -*- coding: utf-8 -*-

import random,string
'''
flag = open("flag", "r").read()
flag_enc = ""
random.seed("​lol​")
for c in flag:
  if c.islower():
    flag_enc += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag_enc += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag_enc += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
    flag_enc += c
with open('output.txt', 'w+') as f:
 f.write("Flag yang sudah dirandom: "+ flag_enc)
'''
flag_enc = "Clrbp7{4kt9m1srj_oqc3b8uew_lf}"
flag = ""
random.seed("​lol​")
for c in flag_enc:
  if c.islower():
    flag += chr((ord(c) - ord('a') - random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag += chr((ord(c) - ord('A') - random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag += chr((ord(c) - ord('0') - random.randrange(0,10))%10 + ord('0'))
  else:
    flag += c

print flag

#((ord(c) - ord('a')) - random.randrange(0,26) + ord('a'))%256)

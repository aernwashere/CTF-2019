#!/usr/bin/python3

import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

getFlag = False
flag = "flag_is_here" 

def activator(key):
	global getFlag
	check_1 = 0
	check_2 = 0
	check_3 = 0
	check_4 = 0
	valid = key.split("-")

	for i in valid[0]:
		if int(i)%2 == 0:
			check_1 += 1
	if int(valid[1]) > 1:
		for i in range(2,int(valid[1])):
			if int(valid[1])%i == 0:
				break
			else:
				check_2 = 1
	if int(valid[2])%4 == 0:
		check_3 = 1
	if valid[3] == "".join(map(chr, [71,75,83,75])):
		check_4 = 1
	if check_1 == 4 and check_2 == 1 and check_3 == 1 and check_4 == 1:
		getFlag = True
		print("Serial is successfully activated! :)")

def validator(key):
	valid = key.split("-")
	checkstrip = [4,9,14]
	checkcode = 0

	for val in valid:
		if len(val) == 4:
			checkcode += 1

	for strip in checkstrip:
		if key[strip] == "-":
			checkcode += 1
		
	if checkcode == 7:
		return True
	else:
		print("Serial isn't valid!")
		return False


def main():
	while True :
		print("1. Get Flag")
		print("2. Enter Activation Code")
		print("3. Exit")
		
		pilih = int(input("Input :"))
		if pilih == 1:
			if getFlag :
				print(flag)
			else:
				print("Enter Activation Code First Bro!")
		elif pilih == 2:
			inp = input("Enter Activation Code :")
			valid_code = validator(inp)
			if valid_code :
				activator(inp)
		elif pilih == 3:
			print("GoodBye! <3")
			exit()
		else:
			print("Error!")
			exit()

if __name__=='__main__':
	main()



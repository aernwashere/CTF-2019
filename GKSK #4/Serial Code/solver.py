'''
XXXX-XXXX-XXXX-XXXX
valid[0,1,2,3]%2 == 0
valid[4,5,6,7]  = 0003
valid[8,9,10,11] = 0004
valid[] = 71,75,83,75
'''

key =  "0000-0003-0004-GKSK"

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

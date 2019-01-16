data1 = [0x30,0x2A,0x35,0x46,0x6E,0x5C,0x59,0x2C,0x2F,0x50,0x4E,0x56,0x62,0x20,0x44,0x20,0x5A]
data2 = [0x0BB2,0x346,0x0B68,0x448,0x12A,0x346,0x402,0x244,0x538,0x54A,0x396,0x64C,0x6EE,0x54A,0x74,0x64C,0x2E0,0x448,0x538,0x64C,0x6EE,0x54A,0x0BE,0x448,0x396,0x244,0x0B68,0x538,0x64C,0x6EE,0x54A,0x0BE,0x448,0x396,0x244,0x0B68]
data3 = [0x20,0x18,0x25,0x31,0x3F,0x0D5,0x0CE,0x0C5,0x3F,0x0E9,0x3F,0x0C4,0x0DB,0x39,0x3F,0x0E6,0x28]

def dee1():
    v6 = [''] * 17
    for i in range(17):
        a1 = data1[i] - i
        a1 ^= 190
        v6[i] = chr(a1)
    return v6

def dee2():
    v7 = [''] * 17
    for j in range(17):
        for i in range(1,256):
            s1 = i & 240
            if (s1 < 0):
                s2 = s1 + 15
            else:
                s2 = s1

            if ((202 * (i & 15) != data2[2 * j]) and (254 * (s2 >> 4) != data2[2 * j +1])):
                continue
            else:
                v7[j] = char(i)
                break
    return v7

def dee3():
    v8 = [0] * 17
    for i in range(17):
        v8[i] = int(data3[i])

    for j in range(1000):
        for k in range(16,-1,-2):
            d1 = v8[(k+1)%17] + 2
            v8[(k+1)%17] = v8[k] + 1
            v8[k] = d1

    return ''.join(chr(x % 256) for x in v8)

if __name__ == '__main__':

    v1 = dee1()
    v2 = dee2()
    v3 = dee3()
    
    print ''.join(v1)
    print ''.join(v2)
    print ''.join(v3)
    flag = ""
    for i in range(17):
        flag += v1[i]
        flag += v2[i]
        flag += v3[i]
    print len(flag)


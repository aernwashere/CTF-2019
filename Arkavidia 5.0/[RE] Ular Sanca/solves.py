data = [''] * 28

data[-2] = 'n'
data[10] = '3'
data[::-2] = '_otp5ar}3l3333'
data[::-3] = '_hpvrtls3r'
data[::-5] = '_yat3v'
data[::-7] = '_{}s'
data[::4] = 'rr_tk{h'
data[::7] = 'r3Ap'

flag = data[14:] + data[:14]

print ''.join(flag)

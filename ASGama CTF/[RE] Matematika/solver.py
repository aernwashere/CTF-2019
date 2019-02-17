from z3 import *
solver = Solver()
s = [''] * 20
for i in range(20):
    d = 's['+str(i)+']'
    s[i]= Int(d)

for i in range(20):
    solver.add(s[i] == i)

print solver.check()
print solver.model()


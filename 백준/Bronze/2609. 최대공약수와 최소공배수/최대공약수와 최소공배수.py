import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

_min = min([n, m])
_max = max([n, m])
r1 = 0
for i in range(1, _min+1):
    if n%i ==0 and m%i==0:
        r1 = i

nn = 2
r2 = 0
omax = _max
while True:

    if _max % _min == 0:
        r2 = _max
        break
    _max = omax* nn
    nn += 1
print(r1)
print(r2)


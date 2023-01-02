import sys
from decimal import Decimal

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    li = list(map(int, input().split(' ')))
    n = li[0]
    x = li[1:]

    if n <= 4:
        print('YES')
        continue
    p = x[0]
    q = x[1]
    r = x[2]
    s = x[3]
    a = -p/6+q/2-r/2+s/6
    b = 3*p/2-4*q+7*r/2-s #Decimal(r-2*q+p-12*a)/Decimal(2)
    c = -13*p/3+19*q/2-7*r+11*s/6 #Decimal(q-p-7*a-3*b)
    d = 4*p-6*q+4*r-s# Decimal(p-a-b-c)
    # print(a, b, c, d)
    for i in range(4, len(x)):
        # print(((i+1)**3)*a+((i+1)**2)*b+(i+1)*c+d, x[i]+0.)
        if round(((i+1)**3)*a+((i+1)**2)*b+(i+1)*c+d) != x[i]:
            print('NO')
            break
    else:
        print('YES')
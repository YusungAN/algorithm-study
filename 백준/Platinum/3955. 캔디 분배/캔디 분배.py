import sys

input = sys.stdin.readline

for i in range(int(input())):
    k, c = map(int, input().split())
    if c == 1:
        print(k+1 if k+1 <= 10**9 else 'IMPOSSIBLE')
        continue
    if k == 1:
        print(1)
        continue
    r0, r1 = c, k
    q0, q1 = 1, 0
    while r1 > 0:
        q = r0//r1
        r0temp = r0
        r0 = r1
        r1 = r0temp-q*r1
        q0temp = q0
        q0 = q1
        q1 = q0temp-q*q1

    if r0 != 1:
        print('IMPOSSIBLE')
    elif q0 < 0:
        print(q0+k)
    else:
        print(q0)
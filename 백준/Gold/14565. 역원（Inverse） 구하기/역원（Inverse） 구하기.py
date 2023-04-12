import sys

input = sys.stdin.readline

n, a = map(int, input().split())
ans1 = n-a

r0, r1 = a, n
c0, c1 = 1, 0
while r1 > 0:
    q = r0//r1
    r0temp = r0
    r0 = r1
    r1 = r0temp-q*r1
    c0temp = c0
    c0 = c1
    c1 = c0temp-q*c1

ans2 = 0
if r0 != 1:
    ans2 = -1
elif c0 < 0:
    ans2 = c0+n
else:
    ans2 = c0
print(ans1, ans2)
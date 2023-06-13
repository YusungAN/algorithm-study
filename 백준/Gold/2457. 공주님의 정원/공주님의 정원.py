import sys

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    li.append((a*100+b, c*100+d))

li.sort()
now_end = 301
cnt = 0
nlen = n
while li:
    now = li[0]
    if now_end >= 1201 or now[0] > now_end:
        break
    next_end = 0
    for i in range(nlen):
        if now_end >= li[0][0]:
            next_end = max(next_end, li[0][1])
            li.remove(li[0])
            nlen -= 1
        else:
            break
    now_end = next_end
    cnt += 1

if now_end >= 1201:
    print(cnt)
else:
    print(0)

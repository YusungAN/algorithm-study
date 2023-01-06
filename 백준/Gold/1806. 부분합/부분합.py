import sys

input = sys.stdin.readline

n, s = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

p1 = 0
p2 = 0

nowsum = li[0]

ans = 0
while p1 <= p2 < n:
    if nowsum >= s and (ans == 0 or p2-p1+1 < ans):
        ans = p2-p1+1

    if nowsum >= s:
        nowsum -= li[p1]
        p1 += 1
    else:
        p2 += 1
        if p2 < n:
            nowsum += li[p2]

print(ans)
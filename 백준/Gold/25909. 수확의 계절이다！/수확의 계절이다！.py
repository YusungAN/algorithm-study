import sys
from collections import defaultdict

input = sys.stdin.readline

dic = defaultdict(int)

coors = []

N, K = map(int, input().split(' '))

x = 0
y = 0
time = 0
end = 0
for _ in range(N):
    a, b = input().rstrip().split(' ')
    b = int(b)
    end += b
    for i in range(b):
        time += 1
        if a == 'E':
            x += 1
        elif a == 'W':
            x -= 1
        elif a == 'N':
            y += 1
        elif a == 'S':
            y -= 1
        if dic[str(x)+' '+str(y)] == 0:
            dic[str(x) + ' ' + str(y)] = time
        else:
            coors.append((x, y, time))


def check(X):
    res = 0
    dictemp = dic.copy()
    for x, y, time in coors:
        if time-dictemp[str(x) + ' ' + str(y)] >= X:
            res += 1
            dictemp[str(x) + ' ' + str(y)] = time

    return res

# print(check(23))
start = 1
ans = -1
while start <= end:
    mid = (start+end)//2
    res = check(mid)
    # print(mid, res)
    if res >= K:
        ans = mid
        start = mid+1
    elif res < K:
        end = mid - 1

print(ans)

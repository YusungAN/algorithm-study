import sys

N = int(sys.stdin.readline().rstrip())
li = []

for i in range(N):
    w, h = map(int, sys.stdin.readline().rstrip().split(' '))
    li.append([w, h])

for i in li:
    cnt = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')


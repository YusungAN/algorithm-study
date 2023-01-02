import sys

T = int(sys.stdin.readline().rstrip())
res = []

def in_circle(cx, cy, r, x, y):
    return (cx-x)**2 + (cy-y)**2 < r**2

for i in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(' '))
    n = int(sys.stdin.readline().rstrip())
    for j in range(n):
        cx, cy, r = map(int, sys.stdin.readline().rstrip().split(' '))
        if in_circle(cx, cy, r, x1, y1) and in_circle(cx, cy, r, x2, y2):
            continue
        if in_circle(cx, cy, r, x1, y1) or in_circle(cx, cy, r, x2, y2):
            cnt += 1
    res.append(cnt)

for i in res:
    print(i)


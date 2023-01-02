import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        arr.append(-1)
    elif (x1-x2)**2 + (y1-y2)**2 == (r1+r2)**2 or (x1-x2)**2 + (y1-y2)**2 == (r1-r2)**2:
        arr.append(1)
    elif (x1-x2)**2 + (y1-y2)**2 > (r1+r2)**2 or (x1-x2)**2 + (y1-y2)**2 < (r1-r2)**2:
        arr.append(0)
    else:
        arr.append(2)

for i in arr:
    print(i)

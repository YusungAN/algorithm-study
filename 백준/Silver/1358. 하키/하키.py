import sys

w, h, x, y, p = map(int, sys.stdin.readline().rstrip().split(' '))
r = h // 2

def isin(x1, y1):
    if x <= x1 and x1 <= x+w and y <= y1 and y1 <= y+h:
        return True
    elif x1 < x and (x1-x)**2 + (y+r-y1)**2 <= r**2:
        return True
    elif x1 > x+w and (x+w-x1)**2 + (y+r-y1)**2 <= r**2:
        return True
    else:
        return False
cnt = 0
for i in range(p):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    if isin(a, b):
        cnt += 1

print(cnt)

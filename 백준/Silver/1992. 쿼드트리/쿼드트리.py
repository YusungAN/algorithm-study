import sys

input = sys.stdin.readline

N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, list(input().rstrip()))))

def allsame(y1, x1, y2, x2):
    temp = li[y1][x1]
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if temp != li[i][j]:
                return False
    return True

def func(y1, x1, n):
    y2 = y1 + n -1
    x2 = x1 + n -1
    if x1 == x2 and y1 == y2:
        return li[y1][x2]
    if allsame(y1, x1, y2, x2):
        return li[y1][x2]

    return '({}{}{}{})'.format(func(y1, x1, n//2), func(y1, x1+n//2, n//2), func(y1+n//2, x1, n//2), func(y1+n//2, x1+n//2, n//2))

print(func(0, 0, N))

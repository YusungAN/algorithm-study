import sys

input = sys.stdin.readline

n = int(input())
c, e = map(int, input().split(' '))

arr = [[0]*n for _ in range(n)]
ccnt = 0
for i in range(n):
    for j in range(i+1):
        if ccnt >= c:
            break
        arr[i-j][j] = 1
        ccnt += 1
    if ccnt >= c:
        break

for i in range(n, 2*n-1):
    for j in range(i-n+1, n):
        if ccnt >= c:
            break
        arr[i-j][j] = 1
        ccnt += 1
    if ccnt >= c:
        break

def is_near_e(x, y, k):
    if x > 0 and arr[y][x-1] == k:
        return True
    if x < n-1 and arr[y][x+1] == k:
        return True
    if y > 0 and arr[y-1][x] == k:
        return True
    if y < n-1 and arr[y+1][x] == k:
        return True
    return False

ecnt = 0

for i in reversed(range(n, 2*n-1)):
    for j in range(i-n+1, n):
        if ecnt >= e:
            break
        arr[j][i-j] = 2
        ecnt += 1
    if ecnt >= e:
        break

if ecnt < e:
    print(-1)
else:
    print(1)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='')
        print('')


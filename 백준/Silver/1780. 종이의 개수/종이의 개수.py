import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split(' '))))
one = 0
zero = 0
minus = 0

def allsame(y1, x1, y2, x2):
    temp = li[y1][x1]
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if temp != li[i][j]:
                return False
    return True

res_temp = []
def func(y1, x1, n):
    y2 = y1 + n -1
    x2 = x1 + n -1
    global one
    global zero
    global minus
    if x1 == x2 and y1 == y2:
        if li[y1][x1] == 1:
            one += 1
        elif li[y1][x1] == 0:
            zero += 1
        else:
            minus += 1
        return
    if allsame(y1, x1, y2, x2):
        if li[y1][x1] == 1:
            one += 1
        elif li[y1][x1] == 0:
            zero += 1
        else:
            minus += 1
        return
    func(y1, x1, n//3)
    func(y1, x1+n//3, n//3)
    func(y1, x1 + 2*(n // 3), n // 3)
    func(y1+n//3, x1, n // 3)
    func(y1+n//3, x1 + n // 3, n // 3)
    func(y1+n//3, x1 + 2 * (n // 3), n // 3)
    func(y1+2*(n//3), x1, n // 3)
    func(y1+2*(n//3), x1 + n // 3, n // 3)
    func(y1+2*(n//3), x1 + 2 * (n // 3), n // 3)

func(0, 0, n)

print(minus)
print(zero)
print(one)

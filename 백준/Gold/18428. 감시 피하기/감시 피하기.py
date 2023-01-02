import sys

input = sys.stdin.readline

n = int(input())
li = []
ts = []
for i in range(n):
    li.append(list(input().rstrip().split(' ')))
    for j in range(n):
        if li[i][j] == 'T':
            ts.append((i, j))

avail_li = []
for y, x in ts:
    if 'S' in li[y]:
        for i in range(x-1, -1, -1):
            if li[y][i] == 'S':
                break
            elif li[y][i] == 'X':
                avail_li.append((y, i))
        for i in range(x, n):
            if li[y][i] == 'S':
                break
            elif li[y][i] == 'X':
                avail_li.append((y, i))

    inS = False
    for i in range(n):
        if li[i][x] == 'S':
            inS = True
            break
    if inS:
        for i in range(y-1, -1, -1):
            if li[i][x] == 'S':
                break
            elif li[i][x] == 'X':
                avail_li.append((i, x))
        for i in range(y, n):
            if li[i][x] == 'S':
                break
            elif li[i][x] == 'X':
                avail_li.append((i, x))


a_set = list(set(avail_li))


def isOk():
    for y, x in ts:
        for i in range(x - 1, -1, -1):
            if li[y][i] == 'O':
                break
            elif li[y][i] == 'S':
                return False
        for i in range(x, n):
            if li[y][i] == 'S':
                return False
            elif li[y][i] == 'O':
                break

        for i in range(y - 1, -1, -1):
            if li[i][x] == 'S':
                return False
            elif li[i][x] == 'O':
                break
        for i in range(y, n):
            if li[i][x] == 'S':
                return False
            elif li[i][x] == 'O':
                break
    return True

visited = [[False]*n for _ in range(n)]

def bt(depth):
    if depth == 3:
        # print(li)
        if isOk():
            print('YES')
            exit(0)
        return

    for y, x in a_set:
        if not visited[y][x]:
            visited[y][x] = True
            li[y][x] = 'O'
            if isOk():
                print('YES')
                exit(0)
            bt(depth+1)
            li[y][x] = 'X'
            visited[y][x] = False

bt(0)
print('NO')


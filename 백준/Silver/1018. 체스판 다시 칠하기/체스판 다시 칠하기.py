import sys
import copy

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
li_original = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    txt = sys.stdin.readline().rstrip()
    for idx, j in enumerate(txt):
        if j == 'B':
            li_original[i][idx] = 1

res = []

def change(num):
    if num == 0:
        return 1
    else:
        return 0


for i in range(n-8+1):
    for j in range(m-8+1):
        li = copy.deepcopy(li_original)
        cnt = 0
        # (0, 0) = W
        if li[i][j] == 1:
            cnt += 1
        li[i][j] = 0
        for k in range(1, 8):
            if li[i][j+k] == li[i][j+k-1]:
                li[i][j+k] = change(li[i][j+k])
                cnt += 1
        for l in range(8):
            for k in range(1, 8):
                if li[i+k][j+l] == li[i+k-1][j+l]:
                    li[i+k][j+l] = change(li[i+k][j+l])
                    cnt += 1

        res.append(cnt)
        if cnt == 30:
            umm = copy.deepcopy(li)
        cnt = 0
        li = copy.deepcopy(li_original)
        # (0, 0) = B
        if li[i][j] == 0:
            cnt += 1
        li[i][j] = 1
        for k in range(1, 8):
            if li[i][j + k] == li[i][j + k - 1]:
                li[i][j + k] = change(li[i][j + k])
                cnt += 1
        for l in range(8):
            for k in range(1, 8):
                if li[i + k][j + l] == li[i + k - 1][j + l]:
                    li[i + k][j + l] = change(li[i + k][j + l])
                    cnt += 1
        res.append(cnt)

print(min(res))

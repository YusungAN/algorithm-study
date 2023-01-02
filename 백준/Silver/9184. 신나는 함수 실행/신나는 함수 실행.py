import sys

input = sys.stdin.readline

in_li = []
while True:
    a, b, c = map(int, input().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    in_li.append([a, b, c])

def if_n(n):
    if n > 20:
        return 20
    elif n <= 0:
        return 0
    else:
        return n

dic = {}


for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i <= 0 or j <= 0 or k <= 0:
                dic[(i, j, k)] = 1
            elif i < j < k:
                dic[(i, j, k)] = dic[(i, j, k-1)]+dic[(i, j-1, k-1)]-dic[(i, j-1, k)]
            else:
                dic[(i, j, k)] = dic[(i-1, j, k)]+dic[(i-1, j-1, k)]+dic[(i-1, j, k-1)]-dic[(i-1, j-1, k-1)]


for i in in_li:
    if i[0] <= 0 or i[1] <= 0 or i[2] <= 0:
        print('w({}, {}, {}) = {}'.format(i[0], i[1], i[2], 1))
    elif i[0] > 20 or i[1] > 20 or i[2] > 20:
        print('w({}, {}, {}) = {}'.format(i[0], i[1], i[2], dic[20, 20, 20]))
    else:
        print('w({}, {}, {}) = {}'.format(i[0], i[1], i[2], dic[i[0], i[1], i[2]]))



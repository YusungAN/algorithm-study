import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    uf = [[i, 1]for i in range(200001)]

    def find(num):
        if uf[num][0] == num:
            return num
        uf[num][0] = find(uf[num][0])
        return uf[num][0]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return uf[y][1]
        uf[y][0] = x
        tmp = uf[y][1]
        uf[y][1] += uf[x][1]
        uf[x][1] += tmp
        return uf[y][1]


    f = int(input())
    names = defaultdict(int)
    idx = 1
    for i in range(f):
        id1, id2 = input().rstrip().split(' ')
        if names[id1] == 0:
           names[id1] = idx
           idx += 1

        if names[id2] == 0:
            names[id2] = idx
            idx += 1

        print(union(names[id1], names[id2]))

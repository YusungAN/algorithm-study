import sys

n = int(sys.stdin.readline().rstrip())
li = []

for i in range(n):
    li.append(tuple(map(int, sys.stdin.readline().rstrip().split(' '))))

li.sort()

for (i, j) in li:
    print(i, j)
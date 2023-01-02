import sys

n = int(sys.stdin.readline().rstrip())
li = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    li.append((b, a))

li.sort()

for (i, j) in li:
    print(j, i)
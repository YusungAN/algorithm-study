import sys

n = int(sys.stdin.readline().rstrip())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort()
for i in li:
    print(i)
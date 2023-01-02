import sys

n = int(sys.stdin.readline().rstrip())
li = [0 for i in range(10001)]


for i in range(n):
    li[int(sys.stdin.readline().rstrip())] += 1

for idx, i in enumerate(li):
    for j in range(i):
        print(idx)

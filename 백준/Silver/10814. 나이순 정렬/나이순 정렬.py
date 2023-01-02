import sys

n = int(sys.stdin.readline().rstrip())
li = [[] for i in range(201)]

for i in range(n):
    age, txt = sys.stdin.readline().rstrip().split(' ')
    li[int(age)].append(txt)

for idx, i in enumerate(li):
    for j in i:
        print(idx, j)


import sys

input = sys.stdin.readline

n = int(input())
ins = []
for i in range(n):
    ins.append(int(input()))

li = [1, 1, 1, 2, 2]

for i in range(5, 100):
    li.append(li[i-1]+li[i-5])

for i in ins:
    print(li[i-1])


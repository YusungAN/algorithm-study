import sys

input = sys.stdin.readline

li = [0.]*10

for i in range(10):
    li[i] = float(input())

li.sort(reverse=True)
res = 10**9
for i in range(len(li)-1):
    res *= li[i]/(i+1)

print(res)

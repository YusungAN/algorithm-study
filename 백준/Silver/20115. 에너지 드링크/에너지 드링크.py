import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split(' ')))
li.sort()
for i in range(N-1):
    li[-1] += li[0]/2
    li.remove(li[0])

print(li[0])
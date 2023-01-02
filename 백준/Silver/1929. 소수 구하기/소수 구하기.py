import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [0 for i in range(0, m+1)]
arr[0] = 1
arr[1] = 1


for i in range(0, m+1):
    if arr[i] == 0:
        for j in range(i*2, m+1, i):
            arr[j] = 1

for i in range(n, m+1):
    if arr[i] == 0:
        print(i)


import sys

input = sys.stdin.readline

n = int(input())
dpmax = list(map(int, input().split()))
dpmin = dpmax[:]
for i in range(1, n):
    a, b, c = map(int, input().split(' '))
    dpmax0 = a+max(dpmax[0], dpmax[1])
    dpmax1 = b + max(dpmax[0], dpmax[1], dpmax[2])
    dpmax2 = c + max(dpmax[1], dpmax[2])
    dpmax[0] = dpmax0
    dpmax[1] = dpmax1
    dpmax[2] = dpmax2
    dpmin0 = a + min(dpmin[0], dpmin[1])
    dpmin1 = b + min(dpmin[0], dpmin[1], dpmin[2])
    dpmin2 = c + min(dpmin[1], dpmin[2])
    dpmin[0] = dpmin0
    dpmin[1] = dpmin1
    dpmin[2] = dpmin2

print(max(dpmax), min(dpmin))
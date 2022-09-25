import sys

input = sys.stdin.readline

fac = [0]*101
fac[0] = 1
for i in range(1, 101):
    fac[i] = fac[i-1]*i

n, m = map(int, input().split(' '))
print(fac[n]//(fac[m]*fac[n-m]))
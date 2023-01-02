import sys

input = sys.stdin.readline

n = int(input())
v = [0]*(10**6+2)
v[2] = 1
v[3] = 1

for i in range(4, 10**6+1):
    if i % 2 == 0 and i % 3 == 0:
        v[i] = min(v[i//2], v[i//3], v[i-1])+1
    elif i % 2 == 0:
        v[i] = min(v[i//2], v[i-1])+1
    elif i % 3 == 0:
        v[i] = min(v[i // 3], v[i - 1]) + 1
    else:
        v[i] = v[i-1]+1

print(v[n])

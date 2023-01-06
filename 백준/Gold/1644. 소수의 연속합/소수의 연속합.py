import sys

input = sys.stdin.readline

n = int(input())
arr = [True]*(4000000+1)
arr[0] = False
arr[1] = False
for i in range(2, int(4000000**(1/2))+1):
    if arr[i]:
        for j in range(i+i, 4000000+1, i):
            arr[j] = False

parr = [idx for idx, i in enumerate(arr) if i]

p1 = 0
p2 = 0
nowsum = parr[0]


cnt = 0
lenparr = len(parr)
while p1 <= p2 < lenparr:
    if nowsum == n:
        cnt += 1

    if nowsum < n:
        p2 += 1
        if p2 < lenparr:
            nowsum += parr[p2]
    else:
        nowsum -= parr[p1]
        p1 += 1

print(cnt)
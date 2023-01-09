import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
lis = [li[0]]
lismap = [(li[0], 1)]
idx = 0

def search(num, r):
    start = 0
    end = r
    while start < end:
        mid = (start+end)//2

        if lis[mid] < num:
            start = mid+1
        else:
            end = mid

    return end


for i in range(1, n):
    if lis[-1] < li[i]:
        lis.append(li[i])
        lismap.append((li[i], len(lis)))
        idx += 1
    else:
        j = search(li[i], idx)
        lis[j] = li[i]
        lismap.append((li[i], j+1))

print(len(lis))

tmp = len(lis)
res = []
for i in range(n-1, -1, -1):
    if lismap[i][1] == tmp:
        res.append(lismap[i][0])
        tmp -= 1

print(*reversed(res))
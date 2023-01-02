import sys

input = sys.stdin.readline

k, n = map(int, input().split(' '))
li = []
for i in range(k):
    li.append(int(input()))

def isOK(m):
    _sum = 0
    for i in li:
        _sum += i // m
    if _sum >= n:
        return True
    else:
        return False


start = 1
end = max(li)
mid = (start+end)//2

max = 0
while start <= end:
    if isOK(mid):
        max = mid
        start = mid+1
    else:
        end = mid-1
    mid = (start+end)//2

print(max)
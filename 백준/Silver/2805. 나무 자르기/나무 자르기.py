import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

def isOK(h):
    _sum = 0
    for i in li:
        _sum += i - h if i - h > 0 else 0
    if _sum >= m:
        return True
    return False



start = 0
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
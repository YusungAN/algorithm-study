import sys

input = sys.stdin.readline

n, c = map(int, input().split(' '))
li = []
for i in range(n):
    li.append(int(input()))
li.sort()

def isOK(k):
    now = li[0]
    cnt = 1
    for i in range(1, n):
        if li[i]-now >= k:
            now = li[i]
            cnt += 1
            #print(now, li[i])
    if cnt >= c:
        return True
    return False


start = 1
end = li[-1]-li[0]
mid = (start+end)//2

max = 0
while start <= end:
    #print('asdf', mid)
    if isOK(mid):
        max = mid
        start = mid+1
    else:
        end = mid-1
    mid = (start+end)//2

print(max)
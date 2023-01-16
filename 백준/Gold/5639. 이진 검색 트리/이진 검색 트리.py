import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)
li = []

while True:
    try:
        li.append(int(input()))
    except:
        break

n = len(li)
def post(l, r):
    if l > r:
        return
    mid = r+1
    for i in range(l+1, r+1):
        if li[l] < li[i]:
            mid = i
            break
    post(l+1, mid-1)
    post(mid, r)
    print(li[l])


post(0, n-1)
import sys

input = sys.stdin.readline

n = int(input())
start = 1
end = n
while start <= end:
    mid = (start+end)//2
    print('? '+str(mid))
    sys.stdout.flush()
    tmp = int(input())
    if 2*tmp == mid:
        print('! '+str(mid))
        break
    elif tmp > mid-tmp:
        start = mid+1
    else:
        end = mid-1


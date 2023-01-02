import sys

input = sys.stdin.readline

a, b = map(int, input().split(' '))

arr = [0]+[1]+[0]*54

for i in range(2, 54+1):
    arr[i] = 2*arr[i-1] + 2**(i-1)

def A(n):
    cnt = 0
    bined = bin(n)
    binlen = len(bined)
    # print(bined)

    for i in range(binlen):
        if bined[i] == '1':
            # print(arr[binlen-i-1], n-2**(binlen-i-1)+1)
            cnt += arr[binlen-i-1] + n-2**(binlen-i-1)+1
            n -= 2**(binlen-i-1)

    return cnt

print(A(b)-A(a-1) if a > 1 else A(b))

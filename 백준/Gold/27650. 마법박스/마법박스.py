import sys

input = sys.stdin.readline

n = int(input())
a = [False,False] + [True]*(n-1)
prime = []
for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
start = 0
end = len(prime)-1
ans = n
while start <= end:
    mid = (start+end)//2
    print('? '+str(prime[mid]))
    sys.stdout.flush()
    a = int(input())
    if a == 1:
        start = mid+1
    else:
        ans = min(ans, prime[mid])
        end = mid-1

print('! '+str(ans))
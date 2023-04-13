n = int(input())
ans = 1
while n > 1:
    ans = (ans*n)%(10**9+7)
    n -= 1
print(ans)
   
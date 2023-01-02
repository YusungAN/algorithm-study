N = int(input())
p = list(map(int, input().split()))
p.sort()

sum = 0
for i in range(N):
    sum += (N-i)*p[i]

print(sum)
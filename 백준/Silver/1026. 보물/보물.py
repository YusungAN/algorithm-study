n = int(input())
A = []
B = []

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B)

sum = 0

for i in range(n):
    sum += A[i]*B[i]

print(sum)
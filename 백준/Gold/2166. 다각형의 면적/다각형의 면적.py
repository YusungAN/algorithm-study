import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(tuple(map(int, input().split(' '))))

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += li[i][0]*li[(i+1)%n][1]
    sum2 += li[i][1]*li[(i+1)%n][0]

print('{:.1f}'.format(abs(sum1-sum2)/2))

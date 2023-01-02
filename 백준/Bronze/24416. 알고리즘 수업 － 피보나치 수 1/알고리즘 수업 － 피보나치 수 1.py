import sys

input = sys.stdin.readline

n = int(input())

cnt1 = 0
cnt2 = 0


def fib1(n) :
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return fib1(n-1) + fib1(n-2)

li = [0, 1, 1]

def fib2(n):
    global cnt2
    for i in range(3, n+1):
        li.append(li[i-1]+li[i-2])
        cnt2 += 1
    return li[n]

fib1(n)
fib2(n)

print(cnt1, cnt2)

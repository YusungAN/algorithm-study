import sys

n = int(sys.stdin.readline().rstrip())
li = []
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)


for i in li:
    g = gcd(i[0], i[1])
    print(i[0]*i[1] // g)

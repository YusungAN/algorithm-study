import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, c = map(int, input().split(' '))
    if c < r:
        temp = r
        r = c
        c = temp
    print(r*c+2*(r*(r+1)*(2*r+1)//6-(r+c)*r*(r+1)//2+r**2*c), -1*r*(2 - 3*c*r + r**2)//3)


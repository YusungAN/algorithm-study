import sys

input = sys.stdin.readline

_min, _max = map(int, input().split(' '))

arr = [0]*(_max-_min+2)
for i in range(2, int(_max**(1/2)+1)):
    sq = i*i
    for j in range((_min//sq)*sq, _max+1, sq):
        if _min <= j <= _max:
            arr[j-_min] = 1

# print("asdf")
cnt2 = 0
for i in arr:
    if i == 0:
        cnt2 += 1

print(cnt2-1)
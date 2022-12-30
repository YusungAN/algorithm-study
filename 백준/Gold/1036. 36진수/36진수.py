import sys
from collections import defaultdict

input = sys.stdin.readline

li = []
for _ in range(int(input())):
    li.append(list(reversed(list(input().rstrip()))))

K = int(input())

dec236 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
       'B': 11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24,
       'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}

todec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
       'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
       'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ch_li = defaultdict(list)

for i in li:
    for idx, j in enumerate(i):
        if len(ch_li[j]) == 0:
            ch_li[j] = [35*(36**idx)-dec236[j]*(36**idx), j]
        else:
            ch_li[j][0] += 35*(36**idx)-dec236[j]*(36**idx)


ch_li2 = []
for i in todec:
    if len(ch_li[i]) > 0:
        ch_li2.append(ch_li[i])
ch_li2.sort(reverse=True)

ch_li3 = []
cnt = 0
idx = 0
while cnt < K:
    cnt += 1
    if idx == len(ch_li2):
        break
    if len(ch_li2[idx]) > 0 and ch_li2[idx][1] == 'Z':
        idx += 1
        cnt -= 1
        continue
    if len(ch_li2[idx]) > 0:
        ch_li3.append(ch_li2[idx][1])
        idx += 1


for i in li:
    for idx, j in enumerate(i):
        if j in ch_li3:
            i[idx] = 'Z'

sum = 0

for i in li:
    for idx, j in enumerate(i):
        sum += dec236[j]*(36**idx)

res = []
if sum == 0:
    print(0)
    exit(0)
while sum > 0:
    res.append(todec[sum % 36])
    sum //= 36

print(''.join(list(reversed(res))))
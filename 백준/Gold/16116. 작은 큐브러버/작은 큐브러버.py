import sys
from collections import deque

input = sys.stdin.readline


def change(l, ch):
    if l[0] == l[1] or l[0] == l[2]:
        print('NO')
        exit(0)
    if ch in l:
        while l[0] != ch:
            temp = l[0]
            l[0] = l[1]
            l[1] = l[2]
            l[2] = temp
    return l

li = []
for _ in range(8):
    li.append(change(input().rstrip().split(' '), 'B'))

mid_batch = []
li.sort()
# print(li)
mid = deque(li[1:4])
mid_batch.append(li[0][1])
mid_batch.append(li[0][2])
cnt = 0
while mid:
    bot, m1, m2 = mid.popleft()
    if m1 == mid_batch[-1]:
        mid_batch.append(m2)
    else:
        mid.append([bot, m1, m2])
    cnt += 1
    if cnt > 20:
        print('NO')
        exit(0)


mid_batch = list(reversed(mid_batch[:4]))
# print(mid_batch)

bot = ''
for i in li[4]:
    if i not in mid_batch:
        bot = i

li2 = []
for i in li[4:]:
    li2.append(change(i, bot))

# print(li2)
mid2 = deque(li2[1:])
mid_batch2 = []
mid_batch2.append(li2[0][1])
mid_batch2.append(li2[0][2])
cnt = 0
while mid2:
    bot, m1, m2 = mid2.popleft()
    if m1 == mid_batch2[-1]:
        mid_batch2.append(m2)
    else:
        mid2.append([bot, m1, m2])
    cnt += 1
    if cnt > 20:
        print('NO')
        exit(0)

# print(mid_batch2)
mid_batch2 = mid_batch2[:4]


def issame(l1, l2):
    for i in range(4):
        if l1[i] != l2[i]:
            return False
    return True

for i in range(4):
    if issame(mid_batch, mid_batch2):
        print('YES')
        exit(0)
    else:
        temp = mid_batch[0]
        mid_batch[0] = mid_batch[1]
        mid_batch[1] = mid_batch[2]
        mid_batch[2] = mid_batch[3]
        mid_batch[3] = temp

print('NO')
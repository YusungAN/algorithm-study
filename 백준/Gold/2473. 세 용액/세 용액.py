import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
li.sort()
idxs = [0, 0, 0]
tar = float('inf')
for i in range(n-2):
    p1 = i+1
    p2 = n-1
    while p1 < p2:
        if tar > abs(li[i]+li[p1]+li[p2]):
            tar = abs(li[i]+li[p1]+li[p2])
            idxs = [li[i], li[p1], li[p2]]

        if li[i]+li[p1]+li[p2] == 0:
            idxs = [li[i], li[p1], li[p2]]
            tar = 0
            break
        elif li[i]+li[p1]+li[p2] > 0:
            p2 -= 1
        else:
            p1 += 1

print(*idxs)
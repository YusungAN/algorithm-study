import sys

input = sys.stdin.readline

a, b = input().rstrip().split(' ')

b = int(b)
a_li = list(a)

per_li = []

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def perm(arr, depth, n, r):
    if depth == r:
        if arr[0] == '0':
            return
        per_li.append(int(''.join(arr)))
        return
    for i in range(depth, n):
        swap(arr, i, depth)
        perm(arr, depth+1, n, r)
        swap(arr, i, depth)

perm(a_li, 0, len(a_li),len(a_li))

# print(per_li)
res = -1
for i in per_li:
    if res < i < b:
        res = i

print(res)
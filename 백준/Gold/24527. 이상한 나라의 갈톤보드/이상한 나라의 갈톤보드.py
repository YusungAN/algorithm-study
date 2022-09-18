import sys

input = sys.stdin.readline

h = int(input())
q, r = map(int, input().split(' '))

res = [0]*(h+2)
depth_cut = [1]+[0]*(h-1)

for i in range(1, h):
    depth_cut[i] = depth_cut[i-1]+i+1

#print(depth_cut)

def search(n):
    if n == 1:
        return 1, 1

    start = 0
    end = h-1
    mid = (start + end) // 2

    while start <= end:
        if depth_cut[mid-1] < n <= depth_cut[mid]:
            return mid+1, n-depth_cut[mid-1]
        if n > depth_cut[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2


#print(search(15), search(10), search(5))
for i in range(q): # n
    a, b = map(int, input().split(' '))
    depth, seq = search(a) # log(n)
    width = h-depth+2
    e = b / width
    #for j in range(seq-1, seq-1+width):
    #    res[j] += e
    res[seq-1] += e
    res[seq-1+width] -= e

sums = [res[0]]+[0]*(h+1)

for i in range(1, h+2):
    res[i] += res[i-1]
    sums[i] = sums[i-1]+res[i]

#print(res, sums)
for i in range(r):
    a, b = map(int, input().split(' '))
    print(sums[b-1]-sums[a-2] if a > 1 else sums[b-1])

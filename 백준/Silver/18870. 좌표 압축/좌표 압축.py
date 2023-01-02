import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split(' ')))
li_sorted = list(set(li))
li_sorted.sort()
dic = {li_sorted[i]: i for i in range(len(li_sorted))}
for i in li:
    print(dic[i], end=' ')

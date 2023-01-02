import sys
from collections import defaultdict

dic = defaultdict(int)
n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split(' ')))
for i in li:
    dic[i] = 1

m = int(sys.stdin.readline().rstrip())
li2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in li2:
    print(dic[i], end=' ')
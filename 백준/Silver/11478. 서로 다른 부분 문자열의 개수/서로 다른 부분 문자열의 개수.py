import sys
from collections import defaultdict

dic = defaultdict(int)
s = sys.stdin.readline().rstrip()
cnt = 0

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        if dic[s[j:j+i]] == 0:
            cnt += 1
            dic[s[j:j+i]] = 1

print(cnt)

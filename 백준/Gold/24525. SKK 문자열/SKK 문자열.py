import sys

input = sys.stdin.readline

s = input().rstrip()
s_len = len(s)
sums = [0]+[0]*s_len
ssum = [0]+[0]*s_len
ksum = [0]+[0]*s_len

min_idx = [1e9]*300001

for i in range(1, s_len+1):
    if s[i-1] == 'S':
        sums[i] = sums[i-1]+2
        ssum[i] = ssum[i - 1] + 1
        ksum[i] = ksum[i - 1]
    elif s[i-1] == 'K':
        sums[i] = sums[i-1]-1
        ksum[i] = ksum[i - 1] + 1
        ssum[i] = ssum[i - 1]
    else:
        sums[i] = sums[i-1]
        ksum[i] = ksum[i - 1]
        ssum[i] = ssum[i - 1]

for i in range(s_len+1):
    min_idx[sums[i]+100000] = min(min_idx[sums[i]+100000], i)

_max = -1
for i in range(s_len):
    l = int(min_idx[sums[i+1]+100000])
    _len = i-l+1
    s_cnt = ssum[i] - ssum[l]
    k_cnt = ksum[i] - ksum[l]
    if s_cnt > 0 and k_cnt > 0:
        _max = max(_max, _len)

print(_max)

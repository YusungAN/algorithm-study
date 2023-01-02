import sys

t = int(sys.stdin.readline().rstrip())
t_arr = [300, 60, 10]
cnt = [0, 0, 0]

for (i, x) in enumerate(t_arr):
    cnt[i] += t // x
    t -= (t // x) * x
if t == 0:
    print(cnt[0], cnt[1], cnt[2])
else:
    print("-1")

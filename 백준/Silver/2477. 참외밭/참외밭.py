import sys

k = int(sys.stdin.readline().rstrip())
li = []
li_w = []
li_h = []

for i in range(6):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    li.append((a, b))
    if a >= 3:
        li_h.append(b)
    else:
        li_w.append(b)

max_w = max(li_w)
max_h = max(li_h)
res_h = 0
res_w = 0

for idx, i in enumerate(li):
    if i[1] == max_w and i[0] <= 2:
        res_w = li[idx-1][1] - li[(idx+1)%6][1] if li[idx-1][1] - li[(idx+1)%6][1] > 0 else li[(idx+1)%6][1] - li[idx-1][1]
    if i[1] == max_h and i[0] >= 3:

        res_h = li[idx-1][1] - li[(idx+1)%6][1] if li[idx-1][1] - li[(idx+1)%6][1] > 0 else li[(idx+1)%6][1] - li[idx-1][1]

print((max_w*max_h-(res_w*res_h))*k)




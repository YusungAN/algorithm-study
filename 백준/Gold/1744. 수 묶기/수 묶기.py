import sys

input = sys.stdin.readline

p_li = []
n_li = []
z_cnt = 0
one_cnt = 0
for _ in range(int(input())):
    a = int(input())
    if a > 0:
        if a == 1:
            one_cnt += 1
        else:
            p_li.append(a)
    elif a < 0:
        n_li.append(a)
    else:
        z_cnt += 1

p_li.sort(reverse=True)
n_li.sort()
# print(p_li)
# print(n_li)
# print(z_cnt)
ans = one_cnt
for i in range(len(p_li)//2):
    ans += p_li[2*i]*p_li[2*i+1]
for i in range(len(n_li)//2):
    ans += n_li[2*i]*n_li[2*i+1]

if len(p_li) % 2 == 1 and len(n_li) % 2 == 1:
    if z_cnt == 0:
        ans += max(p_li[-1]*n_li[-1], p_li[-1]+n_li[-1])
    else:
        ans += p_li[-1]
elif len(p_li) % 2 == 1:
    ans += p_li[-1]
elif len(n_li) % 2 == 1:
    if z_cnt == 0:
        ans += n_li[-1]

print(ans)
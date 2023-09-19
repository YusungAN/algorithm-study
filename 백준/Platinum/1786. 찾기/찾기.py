import sys

input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

ans = []
plen = len(P)
tlen = len(T)
pi = [0]*plen

i = 0
for j in range(1, plen):
    while i > 0 and P[i] != P[j]:
        i = pi[i-1]
    if P[i] == P[j]:
        i += 1
        pi[j] = i

i = 0
for j in range(tlen):
    while i > 0 and P[i] != T[j]:
        i = pi[i-1]
    if P[i] == T[j]:
        i += 1
        if i == plen:
            ans.append(j-i+2)
            i = pi[i-1]

print(len(ans))
print(*ans)
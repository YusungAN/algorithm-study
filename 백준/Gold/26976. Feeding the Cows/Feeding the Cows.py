import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().rstrip()
    ans = ['.']*n

    cnt = 0
    g = -1
    h = -1
    for i in range(n):
        if s[i] == 'G' and i <= g:
            continue
        if s[i] == 'H' and i <= h:
            continue

        for j in range(min(i+k, n-1), max(i-k, 0)-1, -1):
            if ans[j] == '.':
                ans[j] = s[i]
                cnt += 1
                if s[i] == 'G':
                    g = i+2*k
                if s[i] == 'H':
                    h = i+2*k
                break
    print(cnt)
    print(''.join(ans))
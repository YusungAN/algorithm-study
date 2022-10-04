import sys

input = sys.stdin.readline

s = input().rstrip()
s_len = len(s)

s_li = []
for fir_len in range(1, s_len-2):
    for sec_len in range(1, s_len-2):
        if fir_len + sec_len > s_len-1:
            continue
        temp = ''
        temp += s[0:fir_len][::-1]
        temp += s[fir_len:fir_len + sec_len][::-1]
        temp += s[fir_len + sec_len:][::-1]
        s_li.append(temp)

s_li.sort()
print(s_li[0])
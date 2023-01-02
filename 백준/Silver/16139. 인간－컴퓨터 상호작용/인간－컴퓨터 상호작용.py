import sys

input = sys.stdin.readline
s = input().rstrip()
q = int(input())
qs = []
dic = [[0 for i in range(len(s))] for i in range(26)]
dic[ord(s[0])-97][0] = 1
for i in range(1, len(s)):
  idx = ord(s[i])-97
  dic[idx][i] = 1
  for j in range(26):
    dic[j][i] += dic[j][i-1]

for i in range(q):
    ch, a, b = input().split(' ')
    ch = ord(ch)-97
    a, b = int(a), int(b)
    print(dic[ch][b]-(dic[ch][a-1] if a > 0 else 0))
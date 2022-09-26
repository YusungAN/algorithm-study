import sys

input = sys.stdin.readline

s = input().rstrip()

co1 = 0
co2 = 0
op = ''
if s == '0':
    print('W')
    exit(0)
if 'x' not in s:
    if s == '1':
        s = ''
    elif s == '-1':
        s = '-'
    print(s+'x+W')
    exit(0)
for i in range(len(s)):
    if s[i] == 'x':
        co1 = int(s[:i])
        if i < len(s)-1:
            op = s[i+1]
            co2 = int(s[i+2:])

co1 = co1//2
if co1 == 1:
    co1 = ''
elif co1 == -1:
    co1 = '-'
if co2 == 1:
    co2 = ''
elif co2 == -1:
    co2 = '-'

if co2 != 0:
    print(str(co1)+'xx'+op+str(co2)+'x+W')
else:
    print(str(co1)+'xx+W')


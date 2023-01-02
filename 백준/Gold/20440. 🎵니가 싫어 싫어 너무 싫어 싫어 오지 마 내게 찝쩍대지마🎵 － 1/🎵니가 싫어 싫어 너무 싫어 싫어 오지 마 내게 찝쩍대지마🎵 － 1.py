import sys

input = sys.stdin.readline
n = int(input())
li_2d = [[0, 0] for _ in range(n)]
li_1d = [0]*(2*n)
imos = [0]*(2*n+1)

for i in range(n):
    a, b = map(int, input().split(' '))
    li_2d[i][0] = a
    li_2d[i][1] = b
    li_1d[2*i] = a
    li_1d[2*i+1] = b

li_1d_set = list(set(li_1d))
li_1d_set.sort()
dic = {li_1d_set[i]: i for i in range(len(li_1d_set))}
dic_key = list(dic.keys())
# print(dic)

def search(n):
    start = 0
    end = len(dic_key)
    mid = (start+end) // 2

    while start <= end:
        if n == dic[dic_key[mid]]:
            return dic_key[mid]
        elif n > dic[dic_key[mid]]:
            start = mid + 1
        else:
            end = mid - 1

        mid = (start+end) // 2

    print('search err')
    return -1

# print(search(3))

for i in range(n):
    # print(li_1d, li_1d[2*i], li_1d[2*i+1])
    li_2d[i][0] = dic[li_1d[2*i]]
    li_2d[i][1] = dic[li_1d[2*i+1]]
    imos[li_2d[i][0]] += 1
    imos[li_2d[i][1]] -= 1

for i in range(1, 2*n+1):
    # print('imos', i)
    imos[i] += imos[i-1]

imax = imos.index(max(imos))
for i in range(imax+1, 2*n+1):
    # print('max', i)
    if imos[imax] != imos[i]:
        print(imos[imax])
        print(search(imax), search(i))
        break

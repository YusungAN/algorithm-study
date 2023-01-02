s = input()
arr = []
temp = ''

for i in s:
    if i == '+' or i == '-':
        arr.append(int(temp))
        arr.append(i)
        temp = ''
    else:
        temp += i

arr.append(int(temp))

_sum = 0
signal = True

for i in range(len(arr)):
    if arr[i] == '-':
        signal = False
    elif arr[i] == '+':
        pass
    elif signal:
        _sum += arr[i]
    else:
        _sum -= arr[i]

print(_sum)
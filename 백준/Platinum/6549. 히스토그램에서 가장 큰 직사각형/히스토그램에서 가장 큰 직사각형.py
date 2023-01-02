import sys

input = sys.stdin.readline


def func(li, lenli):
    idx = lenli // 2
    #print(li, lenli)
    if lenli == 1:
        #print(li[0])
        return li[0]

    l = idx-1
    r = idx
    cnt = 2
    min_h = min(li[l], li[r])
    max_area = min_h*cnt

    while 0 <= l and r < lenli:
        lh = li[l-1] if l >= 1 else 0
        rh = li[r+1] if r < lenli-1 else 0
        if rh >= lh:
            min_h = min(rh, min_h)
            max_area = max(max_area, min_h*(cnt+1))
            cnt += 1
            r += 1
        else:
            min_h = min(lh, min_h)
            max_area = max(max_area, min_h*(cnt + 1))
            cnt += 1
            l -= 1
    #print(max_area)

    return max(func(li[0:lenli // 2], lenli//2), func(li[lenli // 2:], lenli-(lenli//2)), max_area)


while True:
    li = list(map(int, input().split(' ')))
    if li[0] == 0:
        break
    print(func(li[1:], li[0]))

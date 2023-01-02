import sys

input = sys.stdin.readline

n = int(input())
li = []
cnt = 0

def nqueen():
    global cnt
    if len(li) == n:
        cnt += 1
        return
    i = 0
    while i < n:  # i is x
        is_ok = True
        if len(li) > 0:
            for (j, k) in enumerate(li):  # j is y, k is x
                if k == i or abs(k-i) == abs(len(li)-j):
                    is_ok = False
                    break
            if not is_ok:
                i += 1
                continue
            li.append(i)
            nqueen()
            li.remove(i)
        else:
            li.append(i)
            nqueen()
            li.remove(i)
        i += 1


nqueen()
print(cnt)

import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
m = int(input())
li2 = list(map(int, input().split(' ')))

li.sort()

def search(n):
    start = 0
    end = len(li)-1
    mid = (start+end)//2

    while start <= end:
        if n == li[mid]:
            return 1
        if n > li[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start+end)//2
    return 0

for i in li2:
    print(search(i))
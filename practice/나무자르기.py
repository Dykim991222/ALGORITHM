import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numlist = list(map(int, input().split()))


result = 0
start, end = 0, max(numlist)

while start <= end:
    mid = (start + end)//2
    check = 0

    for i in range(N):
        if numlist[i] > mid:
            check += (numlist[i] - mid)

    if check >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
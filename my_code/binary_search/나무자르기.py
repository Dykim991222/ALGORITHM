N, M = map(int, input().split())
numlist = list(map(int, input().split()))

start, end = min(numlist), max(numlist)

while start <= end:
    mid = (start + end)//2
    check = 0

    for i in range(N):
        if numlist[i] > mid:
            check += (numlist[i] - mid)

    if check == M:
        print(mid)
        break
    if check > M:
        start = mid + 1
    if check < M:
        end = mid - 1

N = int(input())
NL = list(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))

NL.sort()
answer = []

for x in ML:
    start, end = 0, len(NL) - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if x == NL[mid]:
            answer.append(1)
            found = True
            break
        elif x > NL[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not found:
        answer.append(0)

print(*answer)
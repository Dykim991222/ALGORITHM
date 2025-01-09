import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
list = list(map(int, input().split()))
list.sort()

left, right = 0, N - 1
count = 1
answer = []

while left < right:
    for start in range(N):
        left = start
        if list[left] + list[right] > M:
            right -= 1
            continue
        elif list[left] + list[right] < M:
            continue
        else: # list[left] == list[right]
            count += 1
            answer.append([list[left],list[right]])
            right -= 1


print(count)
print(answer)


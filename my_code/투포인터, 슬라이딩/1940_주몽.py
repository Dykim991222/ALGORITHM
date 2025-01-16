import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
list = list(map(int, input().split()))
list.sort()

left, right = 0, N - 1
count = 0
answer = []

while left < right:
    if list[left] + list[right] == M:
        count += 1
        right -= 1
    elif list[left] + list[right] < M:
        left += 1
    else:
        right -= 1

print(count)


import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()

left = 0
right = len(materials) - 1

answer = 0
while left < right:
    result = materials[left] + materials[right]
    if result < M:
        left += 1
    else:
        if result == M:
            answer += 1
        right -= 1

print(answer)

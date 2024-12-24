import sys

input = sys.stdin.readline
N = int(input())
R = int(input())

numbers = list(map(int, input().split()))

candidates = [[0, 0, 0]] * N  # 추천 횟수, 들어온 순서, 학생 번호

for i, number in enumerate(numbers):
    candidates.sort(key=lambda x: (-x[0], -x[1]))

    in_candidates_flag = False
    for candidate in candidates:
        if candidate[2] == number:
            candidate[0] += 1
            in_candidates_flag = True
            break

    if not in_candidates_flag:
        candidates.pop()
        candidates.append([1, i, number])

# print(candidates)
candidates.sort(key=lambda x: x[2])
for candidate in candidates:
    if candidate[2] == 0:
        continue
    print(candidate[2], end=" ")

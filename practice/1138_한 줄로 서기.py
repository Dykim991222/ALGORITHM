import sys
input = sys.stdin.readline

N = int(input().rstrip())
line = list(map(int, input().split()))
answer = [0] * N

for person in range(1, N + 1):
    count = 0
    for i in range(N):
        if answer[i] == 0:
            if count == line[person - 1]:
                answer[i] = person
                break
            count += 1
        else:
            continue

print(" ".join(map(str, answer)))

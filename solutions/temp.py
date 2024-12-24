import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
garodeung = list(map(int, input().split()))

road = []
for i in range(N + 1):
    road.append(0)

for i in garodeung:
    road[i] = 1

max_H = 0
for H in range(1, N + 1):
    for i in garodeung:

        if i - H >= 0:
            road[i - H] = 1

        if i + H <= N:
            road[i + H] = 1

    all_covered = True
    for j in range(N + 1):
        if road[j] == 0:
            all_covered = False
            break

    if all_covered:
        print(H)
        break

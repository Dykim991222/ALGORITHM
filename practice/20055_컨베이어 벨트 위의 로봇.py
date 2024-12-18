import sys

input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0] * N

step = 0

while True:
    step += 1
    
    belt = [belt[-1]] + belt[:-1]
    robots = [0] + robots[:-1]
    robots[-1] = 0

    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0 and belt[i+1] > 0:
            robots[i] = 0
            robots[i + 1] = 1
            belt[i + 1] -= 1
    robots[-1] = 0


    if belt[0] > 0 and robots[0] == 0:
        robots[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(step)
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
pos = list(map(int, input().split()))

start = 1
end = N


def is_possible(h):
    if pos[0] - h > 0:
        return False

    for i in range(1, len(pos)):
        if pos[i] - pos[i - 1] > 2 * h:
            return False

    if N - pos[-1] > h:
        return False

    return True


while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)

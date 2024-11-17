import sys
fastin = sys.stdin.readline

k, n = map(int, fastin().split())
lancables = [int(fastin()) for _ in range(k)]

start = 1
end = max(lancables)

def is_true(test_value):
    if sum([lancable // mid for lancable in lancables]) >= n:
        return True
    else:
        return False

while (start <= end):
    mid = (start + end) // 2
    if is_true(mid):
        start = mid + 1
    else:
        end = mid - 1
print(end)
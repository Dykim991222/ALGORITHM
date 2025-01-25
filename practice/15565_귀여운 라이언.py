import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
line = list(map(int, input().split()))

my_list = defaultdict(int)
min_length = 100000000
left = 0

for right in range(N):
    my_list[line[right]] += 1

    while my_list[1] >= K:
        min_length = min(min_length, right - left + 1)
        my_list[line[left]] -= 1
        if my_list[line[left]] == 0:
            del my_list[line[left]]
        left += 1

print(min_length if min_length != 100000000 else -1)

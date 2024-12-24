import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
word_list = [input().strip() for _ in range(N)]
count_dict = Counter(word_list)

ans = []
for k, v in count_dict.items():
    if len(k) >= M:
        ans.append((k, v))

ans.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for a in ans:
    print(a[0])

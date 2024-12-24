import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
for i in range(N):
    x = input().strip()
    words.append(x)

for word in words:
    if len(word) < M:
        words.remove(word)

count = {}

for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1


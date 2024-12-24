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

keys_list = list(count.keys())
values_list = list(count.values())

total = []

for i in range(len(keys_list)):
    total.append([keys_list[i], values_list[i]])

total[1].sort()
print(total)
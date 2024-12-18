import sys
input = sys.stdin.readline

N = int(input())
mylist = [list(map(int, input().split())) for _ in range(N)]

mylist.sort()

max_x = max(l[0] for l in mylist)

height = [0] * (max_x + 1)

for x, h in mylist:
    height[x] = h

max_height = 0
area = 0
for i in range(max_x + 1):
    max_height = max(max_height, height[i])
    area += max_height

max_height = 0
for i in range(max_x, -1, -1):
    max_height = max(max_height, height[i])
    area -= max_height

print(area)

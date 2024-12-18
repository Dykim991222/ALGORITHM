import sys

input = sys.stdin.readline

line_list = []
answer = 0

N = int(input().strip())
for _ in range(N):
    L, H = map(int, input().split())
    line_list.append([L, H])

line_list.sort()

max_height = 0
for i in range(len(line_list)):
    max_height = max(max_height, line_list[i][1])

answer += max_height

for i in range(len(line_list)):
    if line_list[i][1] == max_height:
        left = line_list[i][0]
        right = line_list[i][0] + 1

left_list = []
right_list = []
for i in range(len(line_list)):
    if line_list[i][0] < left:
        left_list.append(line_list[i])
    if line_list[i][0] > right:
        right_list.append(line_list[i])

print(left_list)
print(right_list)
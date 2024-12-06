import sys
import heapq

input = sys.stdin.readline

n = int(input())
first_list = []
for _ in range(n):
    p, q = map(int, input().split())
    first_list.append([p, q])

#start = 1, end = -1

second_list = []
for i in first_list:
    second_list.append((i[0], 1, i))
    second_list.append((i[1], -1, i))

print(second_list)
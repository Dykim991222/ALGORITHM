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
for i in range(n):
    second_list.append((first_list[0], 1, i))
    second_list.append((first_list[1], -1, i))

print(second_list)
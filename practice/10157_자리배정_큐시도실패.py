import sys
import heapq

answer = 0
impossible = 0
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input().rstrip())

heap = []

for i in range(1, R+1):
    for k in range(1, C+1):
        heapq.heappush(heap, [k, i])

heng = [i for i in range(1, C+1)]
yul = [i for i in range(1, R+1)]

total = []

start_h, start_y = 1, 1
end_h, end_y = C, R

while heap:
    if heap[0][0] == start_h:
        x = heapq.heappop(heap)
        total.append(x)

    start_h += 1

    if heap[1] == end_y:
        x = heapq.heappop(heap)
        total.append(x)
    end_y -= 1
        

    if heap[0] == end_h:
        result = []
        x = heapq.heappop(heap)
        result.append(x)
        result.sort(reverse = True)
        for item in result:
            total.append(item)


    end_h -= 1

    if heap[1] == start_y:
        result = []
        x = heapq.heappop(heap)
        result.append(x)
        result.sort(reverse = True)
        for item in result:
            total.append(item)
    start_y += 1

print(total)
if C * R < K:
    answer = impossible


import heapq
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
pq = []
answer_list = []


for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        if len(pq) > 0:
            answer_list.append(heapq.heappop(pq)[1])
        else:
            answer_list.append(0)

for x in answer_list:
    print(x)

import sys
import heapq
input = sys.stdin.readline
pq = []
answer = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(pq, x)
    else:
        if len(pq)>0:
            answer.append(heapq.heappop(pq))
        else:
            answer.append(0)

for x in answer:
    print(x)
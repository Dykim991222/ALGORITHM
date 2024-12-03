import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
pq = []

for _ in range(N):
    x = list(map(int, input().split()))
    for num in x:
        if len(pq) < N:
            heapq.heappush(pq, num)
        else:
            if num > pq[0]:
                heapq.heappushpop(pq, num)
    


'''for i in range(N):
    for k in range(N):
        heapq.heappush(pq, (-1) * numbers[i][k])'''


'''answer = []
for _ in range(5):
    answer.append(heapq.heappop(pq))'''




print(pq[0])
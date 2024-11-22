import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    x = int(input())
    numbers.append(x)


h = []
for value in numbers:
    heapq.heappush(h, value)

answer = 0
result = []


while len(h)>1:
    answer += heapq.heappop(h)
    answer += heapq.heappop(h)
    heapq.heappush(h, answer)
    
    result.append(answer)
    answer = 0

print(sum(result))
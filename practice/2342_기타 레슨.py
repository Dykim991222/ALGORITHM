import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

print(sum(lectures), max(lectures))

start = max(lectures)
end = sum(lectures)


while start >= end:
    mid = (start + end) // 2

    

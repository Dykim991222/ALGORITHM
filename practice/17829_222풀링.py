import sys
input = sys.stdin.readline

N = int(input().rstrip())

total = []
for y in range(N):
    row = list(map(int, input().split()))
    total.append(row)
print(total)
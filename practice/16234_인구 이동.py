from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

print(board)
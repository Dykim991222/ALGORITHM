import sys

input = sys.stdin.readline

S, P = map(int, input().split())
DNA_long = list(input())
ACGT_count = list(map(int, input().split()))

print(S, P, DNA_long, ACGT_count)
import sys

input = sys.stdin.readline

S, P = map(int, input().split())
seq = input().strip()
constraints = list(map(int, input().split()))
acgt_count = [0, 0, 0, 0]
acgt_mapper = {"A": 0, "C": 1, "G": 2, "T": 3}


def is_satify_const(acgt_count):
    for a, c in zip(acgt_count, constraints):
        if a < c:
            return 0
    return 1


start = 0
end = P - 1

for item in seq[:P]:
    acgt_count[acgt_mapper[item]] += 1

answer = is_satify_const(acgt_count)

while end + 1 < len(seq):
    acgt_count[acgt_mapper[seq[start]]] -= 1
    acgt_count[acgt_mapper[seq[end + 1]]] += 1
    start += 1
    end += 1
    answer += is_satify_const(acgt_count)

print(answer)

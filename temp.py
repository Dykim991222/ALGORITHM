from itertools import permutations

a =[[1, 2], [3, 4], [5, 6]]

for perm in permutations(a, 3):
    for p in perm:
        print(p)
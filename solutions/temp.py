from itertools import combinations
from multiprocessing import Pool

a = ["pppppppppppppppp", "q", "r", "s"]


def get_score(a):
    return a[0] + a[1]


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        result = pool.imap_unordered(get_score, combinations(a, 2))
        for item in result:
            print(item)

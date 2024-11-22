import time


def add(a, b):
    return a + b


start = time.time()

for i in range(300_000_00):
    # c = add(1, 2)
    c = 1 + 2

end = time.time()
elapsed_time = end - start

print(elapsed_time)

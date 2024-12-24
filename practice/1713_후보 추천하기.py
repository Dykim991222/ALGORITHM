import sys

input = sys.stdin.readline

N = int(input().rstrip())
C = int(input().rstrip())

my_list = list(map(int, input().split()))

answer_list = []

for t, number in enumerate(my_list):
    found = False
    for i in range(len(answer_list)):
        if answer_list[i][0] == number:
            answer_list[i][1] += 1
            found = True
            break

    if not found:
        if len(answer_list) < N:
            answer_list.append([number, 1, t])
        else:
            answer_list.sort(key=lambda x: (x[1], x[2]))
            answer_list[0] = [number, 1, t]


answer_list.sort(key=lambda x: x[0])
ppp = [x[0] for x in answer_list]
print(" ".join(map(str, ppp)))

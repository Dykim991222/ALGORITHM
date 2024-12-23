import sys

input = sys.stdin.readline

position = list(map(str, input().split()))

change_alpha = {'A':1,
                'B':2,
                'C':3,
                'D':4,
                'E':5,
                'F':6,
                'G':7,
                'H':8}

reverse_change_alpha = {v:k for k, v in change_alpha.items()}

king = position[0]
king_p = [int(king[1]), change_alpha[king[0]]]

stone = position[1]
stone_p = [int(stone[1]), change_alpha[stone[0]]]

N = int(position[2])
move = []

how_to_move = {'R': [0, 1],
               'L': [0, -1],
               'B': [-1, 0],
               'T': [1, 0],
               'RT': [1, 1],
               'LT': [1, -1],
               'RB': [-1, 1],
               'LB': [-1, -1]}

for i in range(N):
    a = str(input().strip())
    move.append(a)

moving = [how_to_move[x] for x in move]

for p, q in moving:
    
    if (1 <= king_p[0] + p <= 8) and (1 <= king_p[1] + q <= 8) and ((king_p[0] + p != stone_p[0]) or (king_p[1] + q != stone_p[1])):
        king_p[0] += p
        king_p[1] += q
    
    elif ((king_p[0] + p == stone_p[0]) and (king_p[1] + q == stone_p[1])) and (1 <= stone_p[0] + p <= 8 and 1 <= stone_p[1] + q <= 8):
        king_p[0] += p
        king_p[1] += q
        stone_p[0] += p
        stone_p[1] += q
    else:
        continue

print(str(reverse_change_alpha[king_p[1]]) + str(king_p[0]))
print(str(reverse_change_alpha[stone_p[1]]) + str(stone_p[0]))

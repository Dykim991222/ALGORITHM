import sys

input = sys.stdin.readline

king, stone, N = input().strip().split()
N = int(N)
commands = [input().strip() for _ in range(N)]

king_pos = (ord(king[0]) - 65, int(king[1]) - 1)
stone_pos = (ord(stone[0]) - 65, int(stone[1]) - 1)

for command in commands:
    diff_x = 0
    diff_y = 0

    if "R" in command:
        diff_x += 1

    if "L" in command:
        diff_x -= 1

    if "B" in command:
        diff_y -= 1

    if "T" in command:
        diff_y += 1

    new_king_pos = (king_pos[0] + diff_x, king_pos[1] + diff_y)
    if new_king_pos == stone_pos:
        new_stone_pos = (stone_pos[0] + diff_x, stone_pos[1] + diff_y)
    else:
        new_stone_pos = stone_pos

    out_of_bound_flag = False
    for pos in [new_king_pos, new_stone_pos]:
        if pos[0] < 0 or pos[0] >= 8 or pos[1] < 0 or pos[1] >= 8:
            out_of_bound_flag = True
            break

    if not out_of_bound_flag:
        king_pos = new_king_pos
        stone_pos = new_stone_pos

for pos in [king_pos, stone_pos]:
    print(chr(pos[0] + 65) + str(pos[1] + 1))

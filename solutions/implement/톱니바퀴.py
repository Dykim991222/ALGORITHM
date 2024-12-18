import sys

input = sys.stdin.readline


def rotate_gear(gear, direction):
    if direction == -1:
        gear += gear[0]
        gear = gear[1:]

    else:
        gear = gear[-1] + gear[:-1]

    return gear


def check_left(gear_state, gear_number, direction, left_result):
    left_result.add((gear_number, direction))
    gear_number -= 1

    if gear_number == 0:
        return left_result

    if gear_state[gear_number][6] == gear_state[gear_number - 1][2]:
        return left_result

    else:
        return check_left(gear_state, gear_number, -direction, left_result)


def check_right(gear_state, gear_number, direction, right_result):
    right_result.add((gear_number, direction))
    gear_number -= 1

    if gear_number == 3:
        return right_result

    if gear_state[gear_number][2] == gear_state[gear_number + 1][6]:
        return right_result

    else:
        return check_right(gear_state, gear_number + 2, -direction, right_result)


def planning(gear_state, command):
    left_result = set()
    left_result = check_left(gear_state, command[0], command[1], left_result)
    right_result = set()
    right_result = check_right(gear_state, command[0], command[1], right_result)

    result = left_result.union(right_result)
    return result


gear_state = [input().strip() for _ in range(4)]
K = int(input())
commands = [tuple(map(int, input().split())) for _ in range(K)]

for i in range(K):
    command = commands[i]
    result = planning(gear_state, command)
    # print(result)

    for r in result:
        gear_state[r[0] - 1] = rotate_gear(gear_state[r[0] - 1], r[1])


print(
    int(gear_state[0][0])
    + int(gear_state[1][0]) * 2
    + int(gear_state[2][0]) * 4
    + int(gear_state[3][0]) * 8
)

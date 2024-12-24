import sys

input = sys.stdin.readline

S = input().rstrip()

tag_flag = False
new_S = ""
stack = []

for s in S:
    if s == "<":
        tag_flag = True
        while stack:
            new_S += stack.pop()
        new_S += s
        continue
    elif s == ">":
        tag_flag = False
        new_S += s
        continue

    if tag_flag:
        new_S += s
    else:
        if s == " ":
            while stack:
                new_S += stack.pop()
            new_S += " "
        else:
            stack.append(s)

while stack:
    new_S += stack.pop()

print(new_S.rstrip())

connections = [[1, 3], [3, 4], [4, 2], [1, 2]]

connect_dict = {}

for connection in connections:
    if connect_dict.get(connection[0]) is None:
        connect_dict[connection[0]] = [connection[1]]
    else:
        connect_dict[connection[0]].append(connection[1])

    if connect_dict.get(connection[1]) is None:
        connect_dict[connection[1]] = [connection[0]]
    else:
        connect_dict[connection[1]].append(connection[0])

print(connect_dict)
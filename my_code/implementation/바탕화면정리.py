def solution(wallpaper):
    min_x, min_y = len(wallpaper), len(wallpaper[0])
    max_x, max_y = 0, 0


    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)


    return [min_x, min_y, max_x + 1, max_y + 1]
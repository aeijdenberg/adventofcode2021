m = [[int(x) for x in line.strip()] for line in open('input')]
rv = 0
for y in range(len(m)):
    for x in range(len(m[0])):
        if x != 0 and m[y][x] >= m[y][x - 1]:
            continue
        if x != len(m[0]) - 1 and m[y][x] >= m[y][x + 1]:
            continue
        if y != 0 and m[y][x] >= m[y - 1][x]:
            continue
        if y != len(m) - 1 and m[y][x] >= m[y + 1][x]:
            continue
        rv += 1 + m[y][x]
print(rv)
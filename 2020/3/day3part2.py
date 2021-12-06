lines = [line.strip() for line in open('input')]
answer = 1
for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x, y = 0, 0
    trees = 0
    while y < len(lines):
        x = (x + dx) % len(lines[0])
        y += dy
        if y < len(lines):
            if lines[y][x] == '#':
                trees += 1
    answer *= trees
print(answer)
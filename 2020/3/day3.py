lines = [line.strip() for line in open('input')]
dx, dy = 3, 1
x, y = 0, 0
trees = 0
while y < len(lines):
    x = (x + dx) % len(lines[0])
    y += dy
    if y < len(lines):
        if lines[y][x] == '#':
            trees += 1
print(trees)
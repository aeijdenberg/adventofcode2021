x_bit, y_bit = open('input').read().strip().split(' ', 2)[2].split(', ', 1)
x1, x2, y1, y2 = [int(x) for x in x_bit[2:].split('..')] + [int(y) for y in y_bit[2:].split('..')]

def doit(dx, dy):
    x, y = 0, 0

    max_y = y
    while True:
        x += dx
        y += dy

        max_y = max(max_y, y)

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        dy -= 1

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, max_y

        if dx < 0 and x < x1:
            return False, None

        if dx > 0 and x > x2:
            return False, None

        if dy < 0 and y < y1:
            return False, None

zz = -9999999
for dx in range(1, x2):
    for dy in range(-y2, 1000): # pretty dodgy
        got_it, best = doit(dx, dy)
        if got_it:
            if best > zz:
                zz = best
                print(zz)

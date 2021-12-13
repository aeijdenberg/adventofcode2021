dots = set()
state = 0
for line in open('input'):
    if state == 0:
        if line.strip():
            x, y = [int(z) for z in line.split(',')]
            dots.add((x, y))
        else:
            state = 1
    elif state == 1:
        xy, l = line.split(' ')[2].split('=')
        l = int(l)
        new_dots = set()
        if xy == 'x':
            for x, y in dots:
                if x < l:
                    new_dots.add((x, y))
                elif x > l:
                    new_dots.add((l - (x - l), y))
        elif xy == 'y':
            for x, y in dots:
                if y < l:
                    new_dots.add((x, y))
                elif y > l:
                    new_dots.add((x, l - (y - l)))
        dots = new_dots
        print(len(dots))
        break
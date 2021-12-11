o = [[int(x) for x in line.strip()] for line in open('input')]
rv = 0
for step in range(100):
    flash = [(range(len(o)), range(len(o[0])))]
    while len(flash):
        yr, xr = flash.pop()
        for y in yr:
            for x in xr:
                o[y][x] += 1
                if o[y][x] == 10:
                    rv += 1
                    flash.append((range(max(0, y - 1), min(len(o), y + 2)), range(max(0, x - 1), min(len(o[0]), x + 2))))
    for y in range(len(o)):
        for x in range(len(o[0])):
            if o[y][x] > 9:
                o[y][x] = 0
for l in o:
    print(''.join(str(x) for x in l))
print(rv)
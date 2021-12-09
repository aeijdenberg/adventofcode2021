m = [[int(x) for x in line.strip()] for line in open('input')]
b = [[0] * len(m[0]) for i in range(len(m))]
nextb = 1
countbs = {}
done = False
while not done:
    done = True
    for y in range(len(m)):
        for x in range(len(m[0])):
            if b[y][x] or m[y][x] == 9:
                continue
            potb = set()
            us = m[y][x]
            good = True
            for adj_x, adj_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if adj_x >= 0 and adj_x < len(m[0]) and adj_y >= 0 and adj_y < len(m):
                    them = m[adj_y][adj_x]
                    them_b = b[adj_y][adj_x]
                    if them_b:
                        potb.add(them_b)
                    else:
                        if us > them:
                            good = False
            if good and len(potb) < 2:
                if potb:
                    ob = list(potb)[0]
                else:
                    ob = nextb
                    countbs[ob] = 0
                    nextb += 1
                b[y][x] = ob
                countbs[ob] += 1
                done = False
f = sorted(countbs.values())
print(f[-1]*f[-2]*f[-3])

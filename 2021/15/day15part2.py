def bump_line(line, n):
    return ''.join(str(((int(ch) - 1 + n) % 9) + 1) for ch in line)

scale = 5

things = []
for line in open('input'):
    things.append(''.join(bump_line(line.strip(), n) for n in range(scale)))
orig_len = len(things)
for n in range(1, scale):
    for line in things[:orig_len]:
        things.append(bump_line(line, n))

dests = {}
for y in range(len(things)):
    for x in range(len(things[0])):
        for a, b, c, d in [
            (x + 1, y, x, y),
            (x, y + 1, x, y),
            (x, y, x + 1, y),
            (x, y, x, y + 1),
        ]:
            if c < len(things[0]) and d < len(things):
                dd = dests.get('%i,%i' % (a, b), {})
                dd['%s,%i' % (c, d)] = int(things[d][c])
                dests['%i,%i' % (a, b)] = dd

target = '%i,%i' % (len(things[0]) - 1, len(things) - 1)

dist = {'0,0': 0}
todo = set(['0,0'])
while len(todo):
    # print(len(todo))
    k = todo.pop()
    v = dist[k]
    for pd, cst in dests[k].items():
        if dist.get(pd, 99999999999) > v + cst:
            dist[pd] = v + cst
            todo.add(pd)

print(dist[target])
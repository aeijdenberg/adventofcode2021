things = []
for line in open('input'):
    things.append(line.strip())

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
    k = todo.pop()
    v = dist[k]
    for pd, cst in dests[k].items():
        if dist.get(pd, 99999999999) > v + cst:
            dist[pd] = v + cst
            todo.add(pd)

print(dist[target])
edges = {}
for line in open('input'):
    a, b = line.strip().split('-')
    for o, d in [(a, b), (b, a)]:
        s = edges.get(o, set())
        s.add(d)
        edges[o] = s

journeys = [['start']]
finishes = 0
while len(journeys):
    j = journeys.pop()
    for p in edges[j[-1]]:
        if p == 'end':
            finishes += 1
        elif p == 'start': # hmm? can you do this?
            pass # let's assume not
        elif p.upper() == p: # we can happily transit
            journeys.append(j + [p])
        else: # lower
            if p not in j:
                journeys.append(j + [p])

print(finishes)
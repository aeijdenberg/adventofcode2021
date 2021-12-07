groups = ['']
for line in open('input'):
    if line.strip():
        groups[-1] += line
    else:
        groups.append('')

rv = 0
for g in groups:
    people = g.strip().count('\n') + 1
    for ch in set(g):
        if ch.strip():
            if g.count(ch) == people:
                rv += 1
print(rv)
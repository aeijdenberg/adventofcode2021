
lines = [y for y in (x.strip() for x in open('input')) if y]

g, e = 0, 0
for b in range(len(lines[0])):
    g <<= 1
    e <<= 1
    ones = sum(1 for x in lines if x[b] == '1')
    zeros = len(lines)-ones
    if ones > zeros:
        g |= 1
    elif ones < zeros:
        e |= 1
    else:
        raise

print(g*e)

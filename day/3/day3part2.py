
lines = [y for y in (x.strip() for x in open('input')) if y]

def f(candidates, pos, g):
    if len(candidates) == 1:
        return int(candidates[0], 2)
    else:
        target = g(sum(1 for x in candidates if x[pos] == '1'), len(candidates))
        return f([x for x in candidates if x[pos] == target], pos+1, g)

oxy = f(lines, 0, lambda ones, all: '1' if ones >= (all - ones) else '0')
co2 = f(lines, 0, lambda ones, all: '0' if (all - ones) <= ones else '1')

print(oxy*co2)

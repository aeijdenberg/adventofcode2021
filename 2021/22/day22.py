def modify(t, dim, v1, v2):
    l = list(t)
    l[dim] = (v1, v2)
    return tuple(l)

def split_individual(xyz, dim, v):
    for t in xyz:
        if t[dim][0] < v < t[dim][1]:
            yield modify(t, dim, t[dim][0], v)
            yield modify(t, dim, v, t[dim][1])
        else:
            yield t

def split(these, bxyz):
    all_point_list = []
    for dim in range(3):
        all_points = set()
        for z in these:
            all_points.add(z[dim][0])
            all_points.add(z[dim][1])
        all_points.add(bxyz[dim][0])
        all_points.add(bxyz[dim][1])
        all_point_list.append(all_points)
    rv = set([bxyz])
    for dim in range(3):
        for x in all_point_list[dim]:
            these = set(split_individual(these, dim, x))
            rv = set(split_individual(rv, dim, x))
    return these, rv
            

def filter(t, r):
    l = list(list(x) for x in t)
    for u in l:
        if u[1] < -r or u[0] >= r:
            return None
        u[0] = max(u[0], -r)
        u[1] = min(u[1], r + 1)
    return tuple(tuple(x) for x in l)


class Computer(object):
    def __init__(self):
        self.ons = set()
    
    def turn_on(self, t):
        things, new_ones = split(self.ons, t)
        self.ons = things | new_ones

    def turn_off(self, t):
        things, new_ones = split(self.ons, t)
        self.ons = things - new_ones
    
    def count(self):
        return sum(
            (t[0][1] - t[0][0]) * (t[1][1] - t[1][0]) * (t[2][1] - t[2][0])
            for t in self.ons
        )

c = Computer()
c1 = 0
for line in open('input'):
    print(c1, len(c.ons))
    c1 += 1

    instruction, bits = line.strip().split(' ')
    t = tuple(list(tuple(list(idx + int(x) for idx, x in enumerate(dim.split('=')[1].split('..')))) for dim in bits.split(',')))
    t = filter(t, 50)
    if t is not None:
        if instruction == 'on':
            c.turn_on(t)
        else:
            c.turn_off(t)
print(c.count())
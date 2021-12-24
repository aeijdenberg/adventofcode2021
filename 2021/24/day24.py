def chunk(lines):
    rv = []
    for l in lines:
        if l.startswith('inp'):
            chunk = []
            rv.append(chunk)
        chunk.append(l)
    return rv

class PrintableExecutor(object):
    def __init__(self, f, s):
        self.f = f
        self.s = s
    def __call__(self, *args):
        return self.f(*args)
    def __repr__(self):
        return self.s

def get_var(v):
    if v == 'w':
        return lambda r: r[0][0]
    if v == 'x':
        return lambda r: r[0][1]
    if v == 'y':
        return lambda r: r[0][2]
    if v == 'z':
        return PrintableExecutor(lambda r: r[0][3], 'z')
    if v == 'i':
        return PrintableExecutor(lambda r: r[1], 'input')

def add(f, g):
    const_f = None
    const_g = None
    try:
        const_g = g(None)
    except:
        pass
    try:
        const_f = f(None)
    except:
        pass

    if const_g == 0:
        return f

    if const_f == 0:
        return g

    return PrintableExecutor(lambda r: f(r) + g(r), '(%s + %s)' % (repr(f), repr(g)))

def mul(f, g):
    const_g = None
    try:
        const_g = g(None)
    except:
        pass

    if const_g == 0:
        return constant(0)
    if const_g == 1:
        return f

    return PrintableExecutor(lambda r: f(r) * g(r), '(%s * %s)' % (repr(f), repr(g)))

def div(f, g):
    const_g = None
    try:
        const_g = g(None)
    except:
        pass

    if const_g == 1:
        return f
    
    return PrintableExecutor(lambda r: f(r) // g(r), '(%s // %s)' % (repr(f), repr(g)))

def mod(f, g):
    return PrintableExecutor(lambda r: f(r) % g(r), '(%s %% %s)' % (repr(f), repr(g)))

def eql(f, g):
    return PrintableExecutor(lambda r: 1 if f(r) == g(r) else 0, 'int(%s == %s)' % (repr(f), repr(g)))

def constant(z):
    return PrintableExecutor(lambda regs: z, str(z))

def int_or_get_var(regs, arg):
    try:
        return constant(int(arg))
    except:
        return regs[arg]

def make_p(chunk):
    regs = {
        'w': constant(0),
        'x': constant(0),
        'y': constant(0),
        'z': get_var('z'),
    }
    for line in chunk:
        op, argv = line.strip().split(' ', 1)
        arg = argv.split(' ')
        if op == 'inp':
            regs[arg[0]] = get_var('i')
        elif op == 'add':
            regs[arg[0]] = add(regs[arg[0]], int_or_get_var(regs, arg[1]))
        elif op == 'mul':
            regs[arg[0]] = mul(regs[arg[0]], int_or_get_var(regs, arg[1]))
        elif op == 'div':
            regs[arg[0]] = div(regs[arg[0]], int_or_get_var(regs, arg[1]))
        elif op == 'mod':
            regs[arg[0]] = mod(regs[arg[0]], int_or_get_var(regs, arg[1]))
        elif op == 'eql':
            regs[arg[0]] = eql(regs[arg[0]], int_or_get_var(regs, arg[1]))
    return repr(regs['z'])


knowns = {
    13: {0},
    # following will generate if uncommented, but faster to leave in...
    # 12: {16, 17, 18, 19, 20},
    # 11: {0},
    # 10: {12, 13, 14},
    # 9: {352, 353, 354, 355, 326, 327, 328, 329, 378, 379, 380, 381},
    # 8: {9221, 9222, 9223, 9871, 9872, 9873, 9247, 9248, 9249, 9897, 9898, 9899, 8493, 8494, 8495, 9923, 9924, 9925, 8519, 8520, 8521, 9169, 9170, 9171, 8545, 8546, 8547, 9195, 9196, 9197, 9845, 9846, 9847, 8571, 8572, 8573},
    # 7: {352, 353, 354, 355, 326, 327, 328, 329, 378, 379, 380, 381},
    # 6: {12, 13, 14},
    # 5: {353, 379, 327},
    # 4: {8518, 8519, 8520, 8521, 8522, 9194, 9196, 9197, 9870, 9198, 9871, 9872, 9873, 9874, 9195},
    # 3: {239113, 239114, 239115, 239116, 239117, 239118, 239119, 239120, 239121, 239139, 239140, 239141, 239142, 239143, 239144, 239145, 239146, 239147, 239165, 239166, 239167, 239168, 239169, 239170, 239171, 239172, 239173, 256637, 256638, 256639, 256640, 256641, 256642, 256643, 256644, 256645, 256663, 256664, 256665, 256666, 256667, 256668, 256669, 256670, 256671, 256689, 256690, 256691, 256692, 256693, 256694, 256695, 256696, 256697, 256715, 256716, 256717, 256718, 256719, 256720, 256721, 256722, 256723, 256741, 256742, 256743, 256744, 256745, 256746, 256747, 256748, 256749, 221485, 221486, 221487, 221488, 221489, 221490, 221491, 221492, 221493, 221511, 221512, 221513, 221514, 221515, 221516, 221517, 221518, 221519, 221537, 221538, 221539, 221540, 221541, 221542, 221543, 221544, 221545, 221563, 221564, 221565, 221566, 221567, 221568, 221569, 221570, 221571, 221589, 221590, 221591, 221592, 221593, 221594, 221595, 221596, 221597, 239061, 239062, 239063, 239064, 239065, 239066, 239067, 239068, 239069, 239087, 239088, 239089, 239090, 239091, 239092, 239093, 239094, 239095},
    # 2: {8518, 8519, 8520, 8521, 9194, 9195, 9196, 9197, 9198, 9870, 9871, 9872, 9873, 9874, 8522},
    # 1: {353, 379, 327},
    # 0: {12, 13, 14},
}

fs = [eval('lambda z, input: ' + make_p(ch)) for ch in chunk(open('input').read().split('\n'))]

while len(knowns) < 14:
    print(len(knowns), knowns)
    previous_states = set([0])
    for digit, f in enumerate(fs):
        print(digit, len(previous_states))
        cnt = 0
        next_states = set()
        knowns_for_prev = set()
        for pst in previous_states:
            cnt += 1
            if cnt % 100000 == 0:
                print(cnt)
            for i in range(1, 10):
                nst = f(pst, i)
                if digit in knowns:
                    if nst in knowns[digit]:
                        print(digit, 'good to get here is', pst)
                        knowns_for_prev.add(pst)
                    else:
                        continue
                next_states.add(nst)
        previous_states = next_states
        if len(knowns_for_prev):
            knowns[digit - 1] = knowns_for_prev

prev_goods = {0}
rv = ''
for i, f in enumerate(fs):
    good_digs = {}
    for j in range(1, 10):
        for prev_good in prev_goods:
            nst = f(prev_good, j)
            if nst in knowns[i]:
                s = good_digs.get(j, set())
                s.add(nst)
                good_digs[j] = s
    best = max(good_digs.keys())
    rv += str(best)
    prev_goods = good_digs[best]
print(rv)

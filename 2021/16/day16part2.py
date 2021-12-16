s = bin(int('1'+ open('input').read().strip(), 16))[3:]

def packet(x):
    version, x = int(x[:3], 2), x[3:]
    ptype, x = int(x[:3], 2), x[3:]
    if ptype == 4:
        return literal(x)
    else:
        return operator(x, [
            lambda a, b: a + b,
            lambda a, b: a * b,
            lambda a, b: min(a, b),
            lambda a, b: max(a, b),
            None,
            lambda a, b: 1 if (a > b) else 0,
            lambda a, b: 1 if (a < b) else 0,
            lambda a, b: 1 if (a == b) else 0,
        ][ptype])

def operator(x, f):
    do_packets, x = (x[0] == '1'), x[1:]
    if do_packets:
        return packets(x, f)
    else:
        return bounded(x, f)

def packets(x, f):
    subpackets, x = int(x[:11], 2), x[11:]
    rv = None
    for i in range(subpackets):
        z, x = packet(x)
        if rv is None:
            rv = z
        else:
            rv = f(rv, z)
    return rv, x

def bounded(x, f):
    totlen, x = int(x[:15], 2), x[15:]
    subs, x = x[:totlen], x[totlen:]
    rv = None
    while len(subs):
        z, subs = packet(subs)
        if rv is None:
            rv = z
        else:
            rv = f(rv, z)
    return rv, x

def literal(x):
    v = ''
    done = False
    while not done:
        done, x = (x[0] == '0'), x[1:]
        v, x = v + x[:4], x[4:]
    return int(v, 2), x
    
print(packet(s)[0])

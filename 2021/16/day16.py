s = bin(int('1'+ open('input').read().strip(), 16))[3:]

cnt = 0

def packet(x):
    global cnt
    version, x = int(x[:3], 2), x[3:]
    cnt += version
    ptype, x = int(x[:3], 2), x[3:]
    if ptype == 4:
        return literal(x)
    else:
        return operator(x)

def operator(x):
    do_packets, x = (x[0] == '1'), x[1:]
    if do_packets:
        return packets(x)
    else:
        return bounded(x)

def packets(x):
    subpackets, x = int(x[:11], 2), x[11:]
    for i in range(subpackets):
        x = packet(x)
    return x

def bounded(x):
    totlen, x = int(x[:15], 2), x[15:]
    subs, x = x[:totlen], x[totlen:]
    while len(subs):
        subs = packet(subs)
    return x

def literal(x):
    v = ''
    done = False
    while not done:
        done, x = (x[0] == '0'), x[1:]
        v, x = v + x[:4], x[4:]
    return x
    

packet(s)
print(cnt)
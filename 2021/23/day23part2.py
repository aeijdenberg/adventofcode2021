def print_it(s):
    n = """
#############
#ijklmnopqrs#
###a#b#c#d###
  #t#u#v#w#
  #x#y#z#_#
  #e#f#g#h#
  #########
"""
    for l in n.split('\n'):
        print(''.join(s[ch] if ch in s else ch for ch in l))

exits = set([
    'ijkatxe',
    'ijklmbuyf',
    'ijklmnocvzg',
    'ijklmnopqdw_h',
    'extaklmnopqrs',
    'fyubmnopqrs',
    'gzvcopqrs',
    'h_wdqrs',
])
rooms = 'abcdefghtuvwxyz_'
halls = 'ijlnprs'
accept_dests = {
    'A': 'atxe',
    'B': 'buyf',
    'C': 'cvzg',
    'D': 'dw_h',
}

target = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'A',
    'f': 'B',
    'g': 'C',
    'h': 'D',
    'i': '.',
    'j': '.',
    'k': '.',
    'l': '.',
    'm': '.',
    'n': '.',
    'o': '.',
    'p': '.',
    'q': '.',
    'r': '.',
    's': '.',
    't': 'A',
    'u': 'B',
    'v': 'C',
    'w': 'D',
    'x': 'A',
    'y': 'B',
    'z': 'C',
    '_': 'D',
}
lines = open('input').read().split('\n')
state = {
    'a': lines[2][3],
    'b': lines[2][5],
    'c': lines[2][7],
    'd': lines[2][9],
    'e': lines[3][3],
    'f': lines[3][5],
    'g': lines[3][7],
    'h': lines[3][9],
    'i': '.',
    'j': '.',
    'k': '.',
    'l': '.',
    'm': '.',
    'n': '.',
    'o': '.',
    'p': '.',
    'q': '.',
    'r': '.',
    's': '.',
    't': 'D',
    'u': 'C',
    'v': 'B',
    'w': 'A',
    'x': 'D',
    'y': 'B',
    'z': 'A',
    '_': 'C',
}
energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

all_spots = 'abcdefghijklmnopqrstuvwxyz_'
all_move_spots = rooms + halls

all_moves = set([
    (p, q) for p in (rooms + halls) for q in (rooms + halls) if p != q and (p in rooms and q in halls or p in halls and q in rooms)
])

all_paths = {}
for p, q in all_moves:
    found_path = None
    for path in exits:
        pidx = path.find(p)
        qidx = path.find(q)
        if pidx >= 0 and qidx >= 0:
            if pidx < qidx:
                found_path = path[pidx+1:qidx]
            else:
                found_path = path[qidx+1:pidx][::-1]
            break
    if found_path is None:
        raise
    all_paths[(p, q)] = found_path

def move_state(s, p, q):
    return ''.join(s[p] if ch == q else '.' if ch == p else s[ch] for ch in all_spots)

def to_state(s):
    return ''.join(s[ch] for ch in all_spots)

def from_state(s):
    rv = {}
    for idx, ch in enumerate(all_spots):
        rv[ch] = s[idx]
    return rv

s = to_state(state)
w = to_state(target)
pars = {}
scores = {s: 0}
todo = set([s])
c = 0
while len(todo):
    sb = todo.pop()
    if sb == w:
        print(scores[w])
        continue
    s = from_state(sb)
    c += 1
    if c % 1000 == 0:
        print(c, len(todo))

    for p, q in all_moves:
        if s[p] == '.':
            continue
        if s[q] != '.':
            continue
        found_path = all_paths[(p, q)]

        blocked = False
        cur_e = scores[sb] + energy[s[p]]
        for middle in found_path:
            cur_e += energy[s[p]]
            if s[middle] != '.':
                blocked = True
                break
        if blocked:
            continue
        if q in rooms:
            # make sure it is for us, and make sure no one else is there
            our_ads = accept_dests[s[p]]
            if q not in our_ads:
                continue
            only_d = None
            for d in our_ads[::-1]:
                if s[d] == '.' and only_d is None:
                    only_d = d
                if s[d] != '.' and s[d] != s[p]:
                    blocked = True
            if q != only_d:
                continue
            if blocked:
                continue
        
        new_state = move_state(s, p, q)
        if new_state not in scores or scores[new_state] > cur_e:
            pars[new_state] = sb
            scores[new_state] = cur_e
            todo.add(new_state)


print(c)

z = w
n = []
while z is not None:
    n.append(z)
    z = pars.get(z, None)

for s in n[::-1]:
    print_it(from_state(s))
    print(scores[s])

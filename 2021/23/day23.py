def print_it(s):
    n = """
#############
#ijklmnopqrs#
###a#b#c#d###
  #e#f#g#h#
  #########
"""
    for l in n.split('\n'):
        print(''.join(s[ch] if ch in s else ch for ch in l))

exits = set([
    'eakji',
    'eaklmnopqrs',
    'fbmlkji'
    'fbmnopqrs',
    'gconmlkji',
    'gcopqrs',
    'hdqponmlkji',
    'hdqrs',
])
rooms = 'abcdefgh'
halls = 'ijklmnopqrs'
no_stop = set('kmoq')
accept_dests = {
    'A': 'ae',
    'B': 'bf',
    'C': 'cg',
    'D': 'dh',
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
}
energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

def move_state(s, p, q):
    return ''.join(s[p] if ch == q else '.' if ch == p else s[ch] for ch in 'abcdefghijklmnopqrs')

def to_state(s):
    return ''.join(s[ch] for ch in 'abcdefghijklmnopqrs')

def from_state(s):
    rv = {}
    for idx, ch in enumerate('abcdefghijklmnopqrs'):
        rv[ch] = s[idx]
    return rv

s = to_state(state)
w = to_state(target)
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
    for p in rooms:
        if s[p] != '.':
            for path in exits:
                if path[1] == p:
                    path = path[1:]
                if path[0] == p: # we can start moving...
                    cur_e = scores[sb]
                    for q in path[1:]:
                        if s[q] != '.':
                            break
                        cur_e += energy[s[p]]
                        if q not in no_stop:
                            new_state = move_state(s, p, q)
                            if new_state in scores:
                                if cur_e < scores[new_state]:
                                    scores[new_state] = cur_e
                                    todo.add(new_state)
                            else:
                                scores[new_state] = cur_e
                                todo.add(new_state)
    for p in halls:
        if s[p] != '.':
            ad = accept_dests[s[p]]
            # must both be free of other things
            good = True
            for d in ad:
                if s[d] != s[p] and s[d] != '.':
                    good = False
                    break
            if not good:
                continue
            
            if s[ad[1]] == '.': # then must move there
                only_accept = ad[1]
            else:
                only_accept = ad[0]


            for path in exits: # now lets try to return...
                backward = path[::-1]
                spot = backward.find(p)
                if spot >= 0:
                    cur_e = scores[sb]
                    for q in backward[spot+1:]:
                        if s[q] != '.':
                            break
                        cur_e += energy[s[p]]
                        if q == only_accept:
                            new_state = move_state(s, p, q)
                            if new_state in scores:
                                if cur_e < scores[new_state]:
                                    scores[new_state] = cur_e
                                    todo.add(new_state)
                            else:
                                scores[new_state] = cur_e
                                todo.add(new_state)


print(c)
print_it(state)


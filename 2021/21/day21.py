pos = []
scores = []
for line in open('input'):
    _, p, _, _, pp = line.strip().split(' ')
    pos.append(int(pp))
    scores.append(0)

class Die(object):
    def __init__(self):
        self.next = 1
        self.cnt = 0
    def roll(self):
        rv = self.next
        self.next += 1
        if self.next == 101:
            self.next = 1
        self.cnt += 1
        return rv

import sys

d = Die()
while True:
    for player in range(len(pos)):
        result = d.roll() + d.roll() + d.roll()
        pos[player] = ((pos[player] - 1 + result) % 10) + 1
        scores[player] += pos[player]
        if scores[player] >= 1000:
            other = scores[(player + 1) % len(scores)]
            print(other * d.cnt)
            sys.exit(0)

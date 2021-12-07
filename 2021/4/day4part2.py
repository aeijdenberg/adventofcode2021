
def good(z):
    for c in z:
        if c != -1:
            return False
    return True

class Board(object):
    def __init__(self):
        self.rows = []
    def is_won(self):
        for x, row in enumerate(self.rows):
            if good(row):
                return True
            if good(r[x] for r in self.rows):
                return True
        return False
    def mark(self, z):
        for row in self.rows:
            for x, c in enumerate(row):
                if c == z:
                    row[x] = -1
    def score(self):
        rv = 0
        for row in self.rows:
            for c in row:
                if c != -1:
                    rv += c
        return rv
    def draws_to_win(self, input):
        for idx, i in enumerate(input):
            self.mark(i)
            if self.is_won():
                return idx
        return -1

state = 0
numbers = None
boards = []
for l in open('input'):
    l = l.strip()
    if state == 0:
        if len(l):
            numbers = [int(x) for x in l.split(',')]
            state = 1
    elif state == 1:
        if len(l):
            boards[-1].rows.append([int(x) for x in l.split(' ') if x.strip()])
        else:
            boards.append(Board())

best = -1
bb = None
for b in boards:
    score = b.draws_to_win(numbers)
    if score > best:
        best = score
        bb = b

print(bb.score() * numbers[best])

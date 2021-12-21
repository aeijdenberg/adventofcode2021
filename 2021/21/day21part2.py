pos = []
for line in open('input'):
    _, p, _, _, pp = line.strip().split(' ')
    pos.append(int(pp))

# pos, pos, score, score, target
root = (pos[0], pos[1], 0, 0, 21, 0)
universes = set([root])
complete = {}
while len(universes):
    now = universes.pop()
    if now in complete:
        complete[now][0] += 1
    else:
        print(now)
        children = set()
        wins = [0, 0]
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    next_pos = ((now[0] - 1 + i + j + k) % 10) + 1
                    next_score = now[2] + next_pos
                    if next_score >= now[4]:
                        wins[now[5]] += 1
                    else:
                        to_subtract = min(next_score, now[3])
                        children.add((now[1], next_pos, now[3] - to_subtract, next_pos - to_subtract, now[4] - to_subtract, 1 - now[5]))
        complete[now] = [1, wins, children]
        for ch in children:
            universes.add(ch)

answers = {}

# now count all wins
def score(x):
    if x in answers:
        return answers[x]
    else:
        count, wins, children = complete[x]
        rv = [wins[0], wins[1]]
        for ch in children:
            z = score(ch)
            rv = [rv[0] + z[0], rv[1] + z[1]]
        rv = [rv[0] * count, rv[1] * count]
        answers[x] = rv
        return rv

print('done')
print(score(root))

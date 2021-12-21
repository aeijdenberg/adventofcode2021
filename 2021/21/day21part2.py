pos = []
for line in open('input'):
    _, _, _, _, pp = line.strip().split(' ')
    pos.append(int(pp))

answers = {}

def score(x):
    if x in answers:
        return answers[x]
    else:
        wins = [0, 0]
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    next_pos = ((x[0] - 1 + i + j + k) % 10) + 1
                    next_score = x[2] + next_pos
                    if next_score >= x[4]:
                        wins[x[5]] += 1
                    else:
                        to_subtract = min(next_score, x[3])
                        for y, z in enumerate(score((x[1], next_pos, x[3] - to_subtract, next_score - to_subtract, x[4] - to_subtract, 1 - x[5]))):
                            wins[y] += z
        answers[x] = wins
        return wins

print(max(score((pos[0], pos[1], 0, 0, 21, 0))))

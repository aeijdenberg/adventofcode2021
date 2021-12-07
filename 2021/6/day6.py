states = ([0] * 7) + ([0] * 9)
for x in open('input').read().strip().split(','):
    states[int(x)] += 1
for i in range(80):
    states = states[1:7] + [states[0] + states[7]] + states[8:18] + [states[0] + states[7]]
print(sum(states))
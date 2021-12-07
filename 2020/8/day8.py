program = [line.strip().split() for line in open('input')]

acc = 0
pos = 0
seen = set()
while pos not in seen:
    seen.add(pos)
    if program[pos][0] == 'nop':
        pos += 1
    elif program[pos][0] == 'jmp':
        pos += int(program[pos][1])
    elif program[pos][0] == 'acc':
        acc += int(program[pos][1])
        pos += 1
    else:
        raise
print(acc)
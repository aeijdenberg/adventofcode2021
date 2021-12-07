orig = [line.strip().split() for line in open('input')]

for i in range(len(orig)):
    program = [[y for y in x] for x in orig]
    if program[i][0] == 'jmp':
        program[i][0] = 'nop'
    elif program[i][0] == 'nop':
        program[i][0] = 'jmp'
    else:
        continue

    acc = 0
    pos = 0
    seen = set()
    while pos not in seen and pos < len(program):
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
    
    if pos == len(program): 
        print(acc)
        break

lines = [int(x) for x in open('input').read().split('\n') if x]

for idx, number in enumerate(lines):
    if idx < 25:
        continue
    prev = sorted(lines[idx-25:idx])
    done = False
    for i in range(25):
        for j in range(i, 25):
            if prev[i] + prev[j] == number:
                done = True
                break
        if done:
            break
    if not done:
        print(number)
        break

state = 0
m = {}
for line in open('input'):
    if line.strip():
        if state == 0:
            code = line.strip()
        else:
            k, v = line.strip().split(' -> ')
            m[k] = v
    else:
        state = 1

for i in range(10):
    print(len(code))
    next = []
    for i in range(len(code) - 1):
        next.append(code[i])
        next.append(m[code[i:i+2]])
    next.append(code[-1])
    code = ''.join(next)

counts = {}
for ch in code:
    counts[ch] = counts.get(ch, 0) + 1

print(max(counts.values()) - min(counts.values()))
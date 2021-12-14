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

pair_counts = {}
for i in range(len(code) - 1):
    pair_counts[code[i:i+2]] = pair_counts.get(code[i:i+2], 0) + 1
pair_counts[code[-1] + '_'] = 1

for j in range(40):
    next = {}
    for pair, count in pair_counts.items():
        a = pair[0]
        b = pair[1]
        if b == '_':
            next[pair] = next.get(pair, 0) + count
            continue

        r = m[pair]

        left = pair[0] + r
        right = r + pair[1]

        next[left] = next.get(left, 0) + count
        next[right] = next.get(right, 0) + count
    pair_counts = next

counts = {}
for pair, count in pair_counts.items():
    if pair[0] != '_':
        counts[pair[0]] = counts.get(pair[0], 0) + count

print((max(counts.values()) - min(counts.values())))

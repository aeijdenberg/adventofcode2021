groups = [set()]
for line in open('input'):
    if line.strip():
        for ch in line.strip():
            groups[-1].add(ch)
    else:
        groups.append(set())
print(sum(len(s) for s in groups))
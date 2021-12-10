rv = []
for line in open('input'):
    corrupt = False
    stack = []
    for ch in line.strip():
        if ch in '[{(<':
            stack.append(ch)
        elif ch in '}]>)':
            expected = {'(': ')', '<': '>', '{': '}', '[': ']'}[stack.pop()]
            if expected != ch:
                corrupt = True
                break
    if not corrupt:
        score = 0
        while len(stack):
            score *= 5
            score += {'(': 1, '[': 2, '{': 3, '<': 4}[stack.pop()]
        rv.append(score)

rv.sort()
print(rv[len(rv) // 2])
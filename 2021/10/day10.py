rv = 0
for line in open('input'):
    stack = []
    for ch in line.strip():
        if ch in '[{(<':
            stack.append(ch)
        elif ch in '}]>)':
            expected = {'(': ')', '<': '>', '{': '}', '[': ']'}[stack.pop()]
            if expected != ch:
                rv += {')': 3, ']': 57, '}': 1197, '>': 25137}[ch]
                break
print(rv)
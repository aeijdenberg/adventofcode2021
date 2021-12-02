x, y, a = 0, 0, 0
for line in open('input'):
    if line.strip():
        action, amt = line.strip().split(' ')
        if action == 'forward':
            x += int(amt)
            y += a * int(amt)
        elif action == 'down':
            a += int(amt)
        elif action == 'up':
            a -= int(amt)
        else:
            raise ValueError(action)
print(x * y)
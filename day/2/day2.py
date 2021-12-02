x, y = 0, 0
for line in open('input'):
    if line.strip():
        action, amt = line.strip().split(' ')
        if action == 'forward':
            x += int(amt)
        elif action == 'down':
            y += int(amt)
        elif action == 'up':
            y -= int(amt)
        else:
            raise ValueError(action)
print(x * y)
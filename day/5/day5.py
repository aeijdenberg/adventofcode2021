bits = {}
def set_bit(x, y):
    key = '%s_%s' % (x, y)
    bits[key] = 1 + bits.get(key, 0)

for line in open('input'):
    a, b = line.strip().split(' -> ')
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')
    if x1 == x2:
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
            set_bit(x1, y)
    elif y1 == y2:
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
            set_bit(x, y1)

print(sum(1 for x in bits.values() if x > 1))
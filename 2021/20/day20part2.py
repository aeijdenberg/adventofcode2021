state = 0
algo = ''
img = []
for line in open('input'):
    if state == 0:
        if len(line.strip()):
            algo += line.strip()
        else:
            state = 1
    elif state == 1:
        if len(line.strip()):
            img.append(line.strip())

class Image(object):
    def __init__(self, img, default):
        self.img = img
        self.default = default
    
    def __repr__(self):
        return '\n'.join(self.img)

    def get(self, x, y):
        if 0 <= y < len(self.img):
            row = self.img[y]
            if 0 <= x < len(row):
                return row[x]
        return self.default

    def enhance(self, algo):
        extra = 0
        while True:
            extra += 3 # seems reasonable...
            new_img = []
            for y in range(-extra, len(self.img) + extra):
                new_row = ''
                for x in range(-extra, len(self.img[0]) + extra):
                    idx = 0
                    for r in [-1, 0, 1]:
                        for c in [-1, 0, 1]:
                            idx *= 2
                            idx |= 1 if self.get(x + c, y + r) == '#' else 0
                    new_row += algo[idx]
                new_img.append(new_row)

            counts = {'#': 0, '.': 0}
            for row in new_img[:3] + new_img[-3:]:
                for ch in row:
                    counts[ch] += 1
            for row in new_img[1:-1]:
                counts[row[0]] += 1
                counts[row[-1]] += 1

            if counts['#'] == 0:
                return Image(new_img, '.')
            elif counts['.'] == 0:
                return Image(new_img, '#')

    def count(self):
        c = 0
        for row in self.img:
            for ch in row:
                if ch == '#':
                    c += 1
        return c


cur = Image(img, '.')
for i in range(50):
    print(i)
    cur = cur.enhance(algo)

print(cur.count())

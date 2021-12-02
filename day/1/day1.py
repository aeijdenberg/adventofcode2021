last = None
count = 0
for line in open('input'):
    if line.strip() and last is not None and int(line.strip()) > last:
        count += 1
    last = int(line.strip())
print(count)
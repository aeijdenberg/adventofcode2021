last, more_last, super_last = None, None, None
count = 0
for line in open('input'):
    if line.strip() and super_last is not None and int(line.strip()) + last + more_last > (last + more_last + super_last):
        count += 1
    last, more_last, super_last = int(line.strip()), last, more_last
print(count)

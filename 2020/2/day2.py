valid = 0
for line in open('input'):
    policy, password = line.strip().split(': ', 1)
    ranges, letter = policy.split(' ')
    low, high = (int(x) for x in ranges.split('-'))
    c = password.count(letter)
    if low <= c <= high:
        valid += 1
print(valid)
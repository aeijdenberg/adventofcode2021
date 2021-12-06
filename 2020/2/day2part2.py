valid = 0
for line in open('input'):
    policy, password = line.strip().split(': ', 1)
    ranges, letter = policy.split(' ')
    low, high = (int(x) for x in ranges.split('-'))
    c = password.count(letter)
    if (len(password) >= low and password[low-1] == letter) ^ (len(password) >= high and password[high-1] == letter):
        valid += 1
print(valid)
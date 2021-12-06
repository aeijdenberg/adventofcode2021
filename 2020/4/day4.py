passports = [{}]
for line in open('input'):
    if line.strip():
        for part in line.strip().split(' '):
            k, v = part.strip().split(':')
            passports[-1][k] = v
    else:
        passports.append({})
valid = 0
mandatory_fields = set([
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
])
optional_fields = set([
    'cid',
])
def valid(p):
    for m in mandatory_fields:
        if m not in p:
            return False
    for f in p.keys():
        if f not in mandatory_fields and f not in optional_fields:
            return False
    return True

print(sum(1 for p in passports if valid(p)))

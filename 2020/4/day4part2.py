import re
passports = [{}]
for line in open('input'):
    if line.strip():
        for part in line.strip().split(' '):
            k, v = part.strip().split(':')
            passports[-1][k] = v
    else:
        passports.append({})
valid = 0
def in_range(g, low, high):
    def f(x):
        m = g(x)
        if not m:
            return None
        if low <= int(m[0]) <= high:
            return True
    return f
def hgt(g):
    def f(x):
        m = g(x)
        if not m:
            return None
        if x.endswith('cm'):
            h = int(x[:-2])
            return 150 <= h <= 193
        else:
            h = int(x[:-2])
            return 59 <= h <= 76
    return f
mandatory_fields = {
    'byr': in_range(re.compile('^[0-9]{4}$').match, 1920, 2002),
    'iyr': in_range(re.compile('^[0-9]{4}$').match, 2010, 2020),
    'eyr': in_range(re.compile('^[0-9]{4}$').match, 2020, 2030),
    'hgt': hgt(re.compile('^[0-9]+(cm|in)$').match),
    'hcl': re.compile('^#[0-9a-f]{6}$').match,
    'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$').match,
    'pid' :re.compile('^[0-9]{9}$').match,
}
optional_fields = set([
    'cid',
])
def valid(p):
    for m, expr in mandatory_fields.items():
        if m not in p:
            return False
        if not expr(p[m]):
            return False
    for f in p.keys():
        if f not in mandatory_fields and f not in optional_fields:
            return False
    return True

print(sum(1 for p in passports if valid(p)))

import itertools
standard = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

normalised = sorted(sorted(x) for x in standard)

rv = 0
for line in open('input'):
    for p in itertools.permutations('abcdefg'):
        cur = line.strip().upper()
        for idx, ch in enumerate(p):
            cur = cur.replace(chr(ord('A') + idx), ch)
        observations, output = cur.split(' | ')
        if sorted(sorted(x) for x in observations.split(' ')) == normalised:
            a = 0
            for digit in ([standard.index(''.join(sorted(x))) for x in output.split(' ')]):
                a *= 10
                a += digit
            rv += a
            break
print(rv)

        


normals = [
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
rv = 0
for line in open('input'):
    observations, output = line.strip().split(' | ')
    for num in output.split(' '):
        if len(num.strip()) in [len(normals[1]), len(normals[4]), len(normals[7]), len(normals[8])]:
            rv += 1
print(rv)

rules = {}
for line in open('input'):
    outer, inners = line.split(' bags contain ')
    options = inners.strip()[:-1].split(', ')
    rules[outer] = set()
    for option in options:
        if option != 'no other bags':
            rules[outer].add(option.rsplit(' ', 1)[0].split(' ', 1)[1])
            #rules[outer].append((int(option.split(' ', 1)[0]), option.rsplit(' ', 1)[0].split(' ', 1)[1]))

answers = set()

targets = ['shiny gold']
processed = set()
while len(targets):
    target = targets.pop()
    if target in processed:
        continue
    processed.add(target)
    for outer, inner in rules.items():
        if target in inner:
            targets.append(outer)
            answers.add(outer)

print(len(answers))
rules = {}
for line in open('input'):
    outer, inners = line.split(' bags contain ')
    options = inners.strip()[:-1].split(', ')
    rules[outer] = []
    for option in options:
        if option != 'no other bags':
            rules[outer].append((int(option.split(' ', 1)[0]), option.rsplit(' ', 1)[0].split(' ', 1)[1]))

answers = []
targets = ['shiny gold']
while len(targets):
    target = targets.pop()
    answers.append(target)
    for count, thing in rules[target]:
        targets += [thing] * count

print(len(answers) - 1)
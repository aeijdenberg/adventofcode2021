crabs = [int(x) for x in open('input').read().strip().split(',')]
print(min(sum(abs(y - x) for y in crabs) for x in range(min(crabs), max(crabs) + 1)))

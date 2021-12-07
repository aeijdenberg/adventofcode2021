crabs = [int(x) for x in open('input').read().strip().split(',')]
print(min(sum((lambda z: int(z * (z + 1) / 2))(abs(y - x)) for y in crabs) for x in range(min(crabs), max(crabs) + 1)))

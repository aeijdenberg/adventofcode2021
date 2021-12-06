numbers = {}
for line in open('input'):
    n = int(line.strip())
    numbers[n] = numbers.get(n, 0) + 1
for n, v in numbers.items():
    if n == 1010:
        if v > 1:
            print(n * n)
    else:
        t = 2020 - n
        if t in numbers:
            print(n * t)
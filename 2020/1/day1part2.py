numbers = [int(line.strip()) for line in open('input')]
for i, n in enumerate(numbers):
    for j, m in enumerate(numbers[i+1:]):
        t = 2020 - (n + m)
        if t in numbers[j+1:]:
            print(n*m*t)
print(max(int(line[:7].replace('F', '0').replace('B', '1'), 2) * 8 + int(line.strip()[-3:].replace('L', '0').replace('R', '1'), 2) for line in open('input')))

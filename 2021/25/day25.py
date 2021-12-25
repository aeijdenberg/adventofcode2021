def move(board, ch, dx, dy):
    targets = set()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ch:
                nx = (x + dx) % len(board[y])
                ny = (y + dy) % len(board)
                if board[ny][nx] == '.':
                    targets.add((x, y, nx, ny))
    for x, y, nx, ny in targets:
        board[ny][nx] = ch
        board[y][x] = '.'
    return len(targets)


def move_right(board):
    return move(board, '>', 1, 0)

def move_down(board):
    return move(board, 'v', 0, 1)


board = [[ch for ch in line.strip()] for line in open('input')]
count = 0
while True:
    count += 1
    moved = move_right(board)
    moved += move_down(board)
    if moved == 0:
        print("Done", count)
        break

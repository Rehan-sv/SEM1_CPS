def simulate_movement(board_size, moves):
    position = 0
    for move in moves:
        position += move
        if position < 0:
            position = 0
        elif position >= board_size:
            position = board_size - 1
    return position

size = 10
moves = [3, 2, -1, 5, -8, 2]
print(simulate_movement(size, moves))
# Expected: 3
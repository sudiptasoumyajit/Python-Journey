def right_arrow_star_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' * i)

# Example usage:
right_arrow_star_pattern(5)
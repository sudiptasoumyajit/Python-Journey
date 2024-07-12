def up_arrow_star_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

# Example usage:
up_arrow_star_pattern(5)
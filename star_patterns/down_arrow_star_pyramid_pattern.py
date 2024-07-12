def down_arrow_star_pyramid_pattern(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

# Example usage:
down_arrow_star_pyramid_pattern(5)
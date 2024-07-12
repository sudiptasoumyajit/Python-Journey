def inverted_pyramid_star_pattern(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

# Example usage:
inverted_pyramid_star_pattern(5)
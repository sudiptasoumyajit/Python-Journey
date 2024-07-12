def hollow_inverted_star_pyramid_pattern(rows):
    for i in range(rows, 0, -1):
        if i == rows or i == 1:
            print(' ' * (rows - i) + '*' * (2 * i - 1))
        else:
            print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*')

# Example usage:
hollow_inverted_star_pyramid_pattern(5)
def left_arrow_star_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)
    for i in range(rows - 1, 0, -1):
        print('*' * i)

# Example usage:
left_arrow_star_pattern(5)
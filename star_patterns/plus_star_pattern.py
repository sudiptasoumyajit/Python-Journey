def plus_star_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == size // 2 or j == size // 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Example usage:
plus_star_pattern(5)
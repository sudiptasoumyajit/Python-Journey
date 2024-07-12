def x_star_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Example usage:
x_star_pattern(5)
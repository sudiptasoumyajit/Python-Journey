
def pyramid_star_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

pyramid_star_pattern(5)

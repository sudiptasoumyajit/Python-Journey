
def mirrored_right_triangle_star_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

mirrored_right_triangle_star_pattern(5)

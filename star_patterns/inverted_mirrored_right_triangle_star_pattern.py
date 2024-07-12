
def inverted_mirrored_right_triangle_star_pattern(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)

inverted_mirrored_right_triangle_star_pattern(5)
